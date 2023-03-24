from flask import request, Flask
import json

app = Flask(__name__)
#summarizer = GptSummarizer(api_key=GPT_API_KEY, line_min_words=5, min_word_length=6)

@app.route('/detect-bullying', methods=['GET', 'POST'])
def summarize_text():
    if request.method == 'GET':
        text = request.args.get('text')
        if(not text):
            err_msg = 'invalid url pattern for detect-bullying endpoint. ' +\
                      'please try again with: /detect-bullying?text=<yourText>.'
            return err_msg, 400

    if request.method == 'POST':
        try:
            req_json = request.get_json(force=True)
            text = req_json['text']
        except:
            err_msg = 'invalid body pattern. please try again with: {"text": "yourText"}'
            return err_msg, 400
    
    #summary = Summary(content=summarizer.summarize(text))
    #return json.dumps(summary.__dict__)