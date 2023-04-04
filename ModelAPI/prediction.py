from enum import IntEnum

class PredValsIndex(IntEnum):
    TOXIC = 0,
    SEVERE_TOXIC = 1,
    OBSCENE = 2,
    THREAT = 3,
    INSULT = 4,
    IDENTITY_HATE = 5

class Prediction():

    __threshold = 0.4

    def __init__(self, pred_vals):
        self.toxic = True if pred_vals[0][PredValsIndex.TOXIC.value] > self.__threshold else False
        self.severe_toxic = True if pred_vals[0][PredValsIndex.SEVERE_TOXIC.value] > self.__threshold else False
        self.obscene = True if pred_vals[0][PredValsIndex.OBSCENE.value] > self.__threshold else False
        self.threat = True if pred_vals[0][PredValsIndex.THREAT.value] > self.__threshold else False
        self.insult = True if pred_vals[0][PredValsIndex.INSULT.value] > self.__threshold else False
        self.identity_hate = True if pred_vals[0][PredValsIndex.IDENTITY_HATE.value] > self.__threshold else False

class UserPrediction(Prediction):

    def __init__(self, pred_vals):
        super().__init__(pred_vals)

class DbPrediction(Prediction):
    
    def __init__(self, pred_vals, text):
        super().__init__(pred_vals)
        self.text = text