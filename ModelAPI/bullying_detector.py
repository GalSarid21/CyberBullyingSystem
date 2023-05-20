from flask import request, Flask
import Utils.distil_bert_objects as dbo
from ModelAPI.prediction import DbPrediction, UserPrediction
from DAL.post_presentation_data_dal import PostPresentationDataDAL
from DAL.hate_monitor_dal import HateMonitorDAL
import Utils.multithreading as multithreading
from configparser import ConfigParser
from flask_caching import Cache
from flask_cors import CORS
from pathlib import Path
import numpy as np
import json

# create app
app = Flask(__name__)
CORS(app)

# read config and get vlas
config = ConfigParser()
config.read("Data\\local.ini")
labels = int(config.get('BERT', 'NumLabels'))
db_used_ids_max_len = int(config.get('MySQL', 'DbUsedIdsMaxLen'))
max_concurrency = int(config.get('Concurrency', 'MaxConcurrency'))
distilbert = dbo.get_distilbert_configured(config)

# init cache
cache = Cache()
cache.init_app(app=app, config={"CACHE_TYPE": "filesystem",'CACHE_DIR': Path('/tmp')})
cache.set('db_used_ids', [])


@app.route('/api/user-input/detect-bullying', methods=['GET', 'POST'])
async def detect_bullying_from_user():
    try:
        match request.method:
        
            case 'GET':
                text = request.args.get('text')
                if not text:
                    err_msg = 'invalid url pattern for detect-bullying endpoint. ' +\
                              'please try again with: /detect-bullying?text=<your text>.'
                    return err_msg, 400

            case 'POST':
                try:
                    req_json = request.get_json(force=True)
                    text = req_json['text']
                except:
                    err_msg = 'invalid body pattern. please try again with: {"text": "yourText"}'
                    return err_msg, 400
        
        np_text = np.array([text])
        np_label = np.zeros(np_text.shape[0]*labels).reshape(np_text.shape[0], labels)
        text_ds = dbo.TextualInput(np_text, np_label)
        predictions = dbo.predict(distilbert, text_ds)
        prediction_dicts = [UserPrediction(p).__dict__ for p in predictions]
        return json.dumps(prediction_dicts)
    except Exception as e:
        print(e)
        return 'An error accured, please try again later.', 500

@app.route('/api/db-posts/random', methods=['GET'])
async def get_random_db_post():
    try:            
        async_session = dbo.get_async_session(config)
        async with async_session() as session:
            async with session.begin():
                ppd = None
                while ppd is None:
                    ppd_dal = PostPresentationDataDAL(session)
                    max_id = await ppd_dal.get_max_post_id()
                    post_id = np.random.randint(1, max_id)
                    ppd = await ppd_dal.get_post_presentation_data_by_id(post_id)
        return {'id': ppd.id, 'user_name': ppd.user_name, 'content': ppd.content}
    
    except Exception as e:
        print(e)
        return 'An error accured, please try again later.', 500

@app.route('/api/hate-monitors', methods=['GET'])
async def get_hate_monitors():
    
    user_name = request.args.get('user_name')
    if not user_name:
        err_msg = 'invalid url pattern for hate-monitors endpoint. ' +\
                  'please try again with: /hate-monitors?user_name=<your user name>.'
        return err_msg, 400
    
    try:            
        async_session = dbo.get_async_session(config)
        async with async_session() as session:
            async with session.begin():
                hm_dal = HateMonitorDAL(session)
                hms = await hm_dal.get_hate_monitors_by_user_name(user_name)
                if not hms:
                    return '', 204
        hms_dicts = [hm.__repr__() for hm in hms]
        return hms_dicts
    
    except Exception as e:
        print(e)
        return 'An error accured, please try again later.', 500

@app.route('/api/hate-monitors/delete', methods=['GET'])
async def delete_hate_monitors():
    
    id = int(request.args.get('id'))
    if not id:
        err_msg = 'invalid url pattern for hate-monitors endpoint. ' +\
                  'please try again with: /hate-monitors?user_name=<your user name>.'
        return err_msg, 400
    
    try:            
        async_session = dbo.get_async_session(config)
        async with async_session() as session:
            async with session.begin():
                hm_dal = HateMonitorDAL(session)
                await hm_dal.delete_hate_monitor_by_id(id)
        return '', 204 
    
    except Exception as e:
        print(e)
        return 'An error accured, please try again later.', 500

@app.route('/api/hate-monitors/add', methods=['POST'])
async def add_hate_monitor():
    try:
        req_json = request.get_json(force=True)
    except:
        err_msg = 'invalid body pattern.'
        return err_msg, 400
    
    try:            
        async_session = dbo.get_async_session(config)
        async with async_session() as session:
            async with session.begin():
                hm_dal = HateMonitorDAL(session)
                await hm_dal.create_hate_monitor(
                    req_json['source'], req_json['userName'], req_json['content'],
                    req_json['toxic'], req_json['severeToxic'], req_json['obscene'],
                    req_json['threat'], req_json['insult'], req_json['identityHate']
                )
        return '', 201
    
    except Exception as e:
        print(e)
        return 'An error accured, please try again later.', 500
    
@app.route('/api/db-input/detect-bullying', methods=['GET', 'POST'])
async def detect_bullying_from_db():
    try:            
        match request.method:
        
            case 'GET':
                num_texts = int(request.args.get('num_texts'))
                if not num_texts:
                    err_msg = 'invalid url pattern for detect-bullying endpoint. ' +\
                            'please try again with: /detect-bullying?num_texts=<yourNumber>.'
                    return err_msg, 400

            case 'POST':
                try:
                    req_json = request.get_json(force=True)
                    num_texts = int(req_json['num_texts'])
                except:
                    err_msg = 'invalid body pattern. please try again with: {"num_texts": "yourNumber"}'
                    return err_msg, 400

        async_session = dbo.get_async_session(config)
        async with async_session() as session:
            async with session.begin():
                db_used_ids = cache.get('db_used_ids')
                ppd_dal = PostPresentationDataDAL(session)
                ppds = await ppd_dal.get_top_n_post_presentation_data(db_used_ids, num_texts)
                ids = [ppd.id for ppd in ppds]
                db_used_ids.extend(ids)
                cache.set('db_used_ids', db_used_ids)
                if len(db_used_ids) == db_used_ids_max_len:
                    cache.set('db_used_ids', [])

        num_splits = len(ppds) if len(ppds) <= max_concurrency else max_concurrency
        predictions_dto = multithreading.split_processing(
            items=ppds, task=predict_ppd, num_splits=num_splits)
        return json.dumps(predictions_dto)
    
    except Exception as e:
        print(e)
        return 'An error accured, please try again later.', 500
    
# run server on debug 
def run_server_test():
    app.run()

def predict_ppd(ppd):
    np_text = np.array([ppd.content])
    np_label = np.zeros(np_text.shape[0]*labels).reshape(np_text.shape[0], labels)
    text_ds = dbo.TextualInput(np_text, np_label)
    prediction = dbo.predict(distilbert, text_ds)
    prediction_dto = DbPrediction(prediction[0], ppd.content).__dict__
    return prediction_dto
