import numpy as np

class LinearRegression():
    def __init__(self):
        self.isTrained = False
        self.theta = None
        self.bias = None
        self.loss_hist= None
    
    def fit(self, X, y, learning_rate=0.1, num_iters=1000):
        assert len(X.shape) == 2, 'X must be 2-dimensional of shape (num_samples,num_features)'
        assert len(y.shape) == 1, 'y must be 1-dimensional vector of shape (num_samples,)'
        assert y.shape[0] == X.shape[0], 'num_samples must be same in X and y'
        num_samples = X.shape[0]
        num_features = X.shape[1]
        self.theta = np.zeros(num_features)
        self.bias = np.array([1.0])
        self.loss_hist = np.zeros(num_iters)
        self.isTrained = True
        for i in range(num_iters):
            predictions = self.predict(X)
            self.theta = self.theta - (1/num_samples)*learning_rate*(np.matmul(X.T,predictions-y))
            self.bias = self.bias - (1/num_samples)*learning_rate*(np.matmul(np.ones([num_samples,1]).T,predictions-y))
            self.loss_hist[i] = self.loss(X,y)
        return self.loss_hist
    
    def predict(self, X):
        if self.isTrained is False:
            raise RuntimeError('You must fit the model first before predicting.')
        return np.matmul(X,self.theta) + self.bias

    def loss(self,X,y):
        num_samples = X.shape[0]
        predictions = self.predict(X)
        return (1/(2*num_samples))*np.sum((predictions-y)**2)

class LogisticRegression():
    def __init__(self):
        self.isTrained = False
        self.theta = None
        self.bias = None
        self.loss_hist= None
    
    def fit(self, X, y, learning_rate=0.1, num_iters=1000):
        assert len(X.shape) == 2, 'X must be 2-dimensional of shape (num_samples,num_features)'
        assert len(y.shape) == 1, 'y must be 1-dimensional vector of shape (num_samples,)'
        assert y.shape[0] == X.shape[0], 'num_samples must be same in X and y'
        num_samples = X.shape[0]
        num_features = X.shape[1]
        self.theta = np.zeros(num_features)
        self.bias = np.array([1.0])
        self.loss_hist = np.zeros(num_iters)
        self.isTrained = True
        for i in range(num_iters):
            # 
            # 
            # Complete predict, log_loss, sigmoid code below and use there to train.
            # 
            self.loss_hist[i] = self.log_loss(X,y)
        return self.loss_hist
    
    def predict(self, X):
        if self.isTrained is False:
            raise RuntimeError('You must fit the model first before predicting.')
        predictions = None
        # 
        # 
        # Complete code
        # 
        #
        return predictions
    
    def log_loss(self,X,y):
        loss = None
        # 
        # 
        # Complete code
        # 
        #
        return loss

    def sigmoid(self,X):
        sig = None
        # 
        # 
        # Complete code
        # 
        #
        return sig

    def predict_proba(self, X):
        if self.isTrained is False:
            raise RuntimeError('You must fit the model first before predicting.')
        predictions_probs = None
        # 
        # 
        # Complete code
        # 
        #
        return predictions_probs