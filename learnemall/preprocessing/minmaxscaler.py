# Importing libraries
import numpy as np

class MinMaxScalar():
    """
    :__init__(): Initializes the the class variables 'min' and 'max' (both of array type) 
        with the minimum and maximum values of the each of the features of training class X. It takes
        input as a numpy array.
    :scale(): It scales the features of the training data into the the scale from 0 to 1.
        It takes numpy array as input as well as returns a numpy array consisting of scaled values     
    :revert(): It reverts the input data(already scaled) back into the scale of original data
        It takes input as a numpy array as well as returns a numpy array consisting of reverted values 
        (i.e. it makes the features back into original range of data (range of X) ) 
    """
    def __init__(self,X):
        self.min=np.min(X,axis=0)
        self.max=np.max(X,axis=0)

    def scale(self,dat):
        z = np.zeros(np.shape(dat),dtype=float)
        for i in range(np.shape(dat)[-1]):
            z[:,i] = (dat[:,i]-(np.min(dat,axis=0)[i]))/(np.max(dat,axis=0)[i] - np.min(dat,axis=0)[i])
        return z

    def revert(self,dat):
        z = np.zeros(np.shape(dat),dtype=float)
        for i in range(np.shape(dat)[-1]):
            z[:,i] = ((dat[:,i]*(self.max[i] - self.min[i]))+self.min[i])
        return z