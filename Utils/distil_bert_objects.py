# region Imports
import torch
import torch.nn as nn
from transformers import DistilBertModel,DistilBertTokenizer
from torch.utils.data import Dataset
# endregion


class DistilBertForSequenceClassification(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.num_labels = config.num_labels

        self.distilbert = DistilBertModel.from_pretrained('distilbert-base-uncased')
        self.pre_classifier = nn.Linear(config.hidden_size, config.hidden_size)
        self.classifier = nn.Linear(config.hidden_size, config.num_labels)
        self.dropout = nn.Dropout(config.seq_classif_dropout)

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
    def __init__(self, x, y, transform=None):
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
