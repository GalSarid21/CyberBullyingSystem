#region Imports
import os
import torch
import asyncio
import numpy as np
from Utils.distil_bert_objects import DistilBertForSequenceClassification, TextualInput, predict
import Tests.post_presentation_data_test as ppdt
from DAL.db_clients import SocialMediaDbClient
from configparser import ConfigParser
# endregion


def run_app_test():
    base_path = f"{os.path.abspath(os.curdir)}"
    weights_file_path = f"{base_path}\\Data\\distilbert_model_weights_ver2.pth"
    
    config = ConfigParser()
    config.read("Data\\local.ini")
    distilbert = DistilBertForSequenceClassification(config)
    distilbert.load_state_dict(torch.load(weights_file_path, map_location=torch.device('cpu')))
    
    db_client = SocialMediaDbClient(config)
    session = db_client.get_async_session()
    res = asyncio.run(ppdt.get_post_presentation_data_by_id_test(session, 3))
    input_text = np.array([res.content])
    input_label = np.zeros(input_text.shape[0]*6).reshape(input_text.shape[0],6)
    test_ds = TextualInput(input_text, input_label)

    preds = predict(distilbert, test_ds)
    print(preds)