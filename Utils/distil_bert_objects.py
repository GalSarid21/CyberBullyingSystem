import os
import torch
import torch.nn as nn
from transformers import DistilBertModel, DistilBertTokenizer, DistilBertConfig
from DAL.db_clients import SocialMediaDbClient
from torch.utils.data import Dataset


class DistilBertForSequenceClassification(nn.Module):
    
    def __init__(self, config):
        super().__init__()
        
        distil_bert_config = DistilBertConfig(
                vocab_size_or_config_json_file = int(config.get('BERT', 'VocabSize')), 
                hidden_size = int(config.get('BERT', 'HiddenSize')),
                dropout = float(config.get('BERT', 'Dropout')), 
                num_labels = int(config.get('BERT', 'NumLabels')), 
                num_hidden_layers = int(config.get('BERT', 'NumHiddenLayers')), 
                num_attention_heads = int(config.get('BERT', 'NumAttentionHeads')), 
                intermediate_size = int(config.get('BERT', 'IntermediateSize')))
        
        self.num_labels = distil_bert_config.num_labels
        self.distilbert = DistilBertModel.from_pretrained('distilbert-base-uncased')
        self.pre_classifier = nn.Linear(distil_bert_config.hidden_size, distil_bert_config.hidden_size)
        self.classifier = nn.Linear(distil_bert_config.hidden_size, distil_bert_config.num_labels)
        self.dropout = nn.Dropout(distil_bert_config.seq_classif_dropout)

        nn.init.xavier_normal_(self.classifier.weight)
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    def forward(self, input_ids=None, attention_mask=None, head_mask=None, labels=None):
        distilbert_output = self.distilbert(input_ids=input_ids,
                                            attention_mask=attention_mask,
                                            head_mask=head_mask)
        hidden_state = distilbert_output[0]                    
        pooled_output = hidden_state[:, 0]                   
        pooled_output = self.pre_classifier(pooled_output)   
        pooled_output = nn.ReLU()(pooled_output)             
        pooled_output = self.dropout(pooled_output)        
        logits = self.classifier(pooled_output) 
        return logits


class TextualInput(Dataset):
    
    def __init__(self, x, y, transform = None):
        self.x = x
        self.y = y
        self.transform = transform
        self.max_seq_length = 256
        self.tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
        
    def __getitem__(self, index):
        tokenized_input = self.tokenizer.tokenize(self.x[index])
        
        if len(tokenized_input) > self.max_seq_length:
            tokenized_input = tokenized_input[:self.max_seq_length]

        padding = [0] * (self.max_seq_length - len(tokenized_input))
        tokenized_input += padding
        tokenized_input = self.tokenizer.encode_plus(tokenized_input, add_special_tokens=True, return_tensors='pt')
        ids_review = tokenized_input['input_ids']
    
        hcc = self.y[index]       
        list_of_labels = [torch.from_numpy(hcc)]
        return ids_review, list_of_labels[0]
    
    def __len__(self):
        return len(self.x)


def predict(model, data_loader):
        model.eval()
        predictions = []
        for input, sentiment in data_loader:
            input = input.to(model.device)
            sentiment = sentiment.to(model.device)
            with torch.no_grad():
                outputs = model(input)
                outputs = torch.sigmoid(outputs)
                predictions.append(outputs.cpu().detach().numpy().tolist())
        model.train()
        return predictions

def get_distilbert_configured(config):
    base_path = f"{os.path.abspath(os.curdir)}"
    weights_file_path = f"{base_path}\\Data\\distilbert_model_weights.pth"
    
    distilbert = DistilBertForSequenceClassification(config)
    distilbert.load_state_dict(torch.load(weights_file_path, map_location=torch.device('cpu')))
    
    return distilbert

def get_async_session(config):
    db_client = SocialMediaDbClient(config)
    async_session = db_client.get_async_session()
    return async_session
