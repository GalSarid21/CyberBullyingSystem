#region Imports
import os
import torch
import numpy as np
from transformers import DistilBertConfig
from Utils.distil_bert_objects import DistilBertForSequenceClassification, TextualInput, predict
# endregion


def run_app_test():
    base_path = f"{os.path.abspath(os.curdir)}"
    weights_file_path = f"{base_path}\\Data\\distilbert_model_weights.pth"
    
    config = DistilBertConfig(vocab_size_or_config_json_file=32000, hidden_size=768,
                              dropout=0.1, num_labels=6, num_hidden_layers=12, 
                              num_attention_heads=12, intermediate_size=3072)
    distilbert = DistilBertForSequenceClassification(config)
    distilbert.load_state_dict(torch.load(weights_file_path, map_location=torch.device('cpu')))
    
    input_text = np.array(["this is a test"])
    input_label = np.zeros(input_text.shape[0]*6).reshape(input_text.shape[0],6)
    test_ds = TextualInput(input_text, input_label)

    preds = predict(distilbert, test_ds)