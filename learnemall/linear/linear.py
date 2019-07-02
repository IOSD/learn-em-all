import numpy as np

class LinearRegression():
    def __init__(self):
        self.isTrained = False
    
    def fit(self, features, targets):
        # 
        # 
        # Complete code
        # 
        # 
        self.isTrained = True
        return self
    
    def predict(self, features):
        if self.isTrained is False:
            raise RuntimeError('You must fit the model first before predicting.')
        predictions = None
        # 
        # 
        # Complete code
        # 
        #
        return predictions

class LogisticRegression():
    def __init__(self):
        self.isTrained = False
    
    def fit(self, features, targets):
        # 
        # 
        # Complete code
        # 
        # 
        self.isTrained = True
        return self
    
    def predict(self, features):
        if self.isTrained is False:
            raise RuntimeError('You must fit the model first before predicting.')
        predictions = None
        # 
        # 
        # Complete code
        # 
        #
        return predictions
    
    def predict_proba(self, features):
        if self.isTrained is False:
            raise RuntimeError('You must fit the model first before predicting.')
        predictions_probs = None
        # 
        # 
        # Complete code
        # 
        #
        return predictions_probs