#importing libraries
import numpy as np

  
class StandardScaler:

    def __init__(self,X):
        self.mean=np.mean(X,axis=0)
        self.std=np.std(X,axis=0)

    def scale(self,dat):
        z = np.zeros(np.shape(dat),dtype=float)
        for i in range(np.shape(dat)[-1]):
            z[:,i] = (dat[:,i]-(np.mean(dat,axis=0)[i]))/(np.std(dat,axis=0)[i])

        return z

    def revert(self,dat):
        z = np.zeros(np.shape(dat),dtype=float)
        for i in range(np.shape(dat)[-1]):
            z[:,i] = ((dat[:,i]*(self.std[i]))+self.mean[i])

        return z
    
    
