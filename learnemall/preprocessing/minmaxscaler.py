# class to scale the datasets in the range from [0,1] through scale() function and
# unscaling the data into the same range as of original data through revert() function




#importing libraries

import numpy as np


# from datasets.iris import load_data                # importing the iris datasets through load function to check the
                                                     # correct working of minmaxscalar class here


"""


class minmaxscalar

 the __init__() method   initialises the the class variables 'min' and 'max' (both of array type) 
 with the minimum and maximum values of the each of the features of training class X. It takes
 input as a numpy array.
 
 the scale() function scales the features of the training data into the the scale from 0 to 1.
 it takes numpy array as input as well as returns a numpy array consisting of scaled values     

 the revert() function reverts the input data(already scaled) back into the scale of original data
 it takes input as a numpy array as well as returns a numpy array consisting of reverted values 
 (i.e. it makes the features back into original range of data (range of X) ) 



"""



class MinMaxScalar:

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





"""


   
X,y = load_data(split = False ,ratio = None ,path ="./datasets/data/iris.csv")    
                                                             #loads the dataset from the path and sets X as training set 


mms = MinMaxScalar(X)                                           #initialise the mms class to work upon training data X                                                   
                                                                (i.e. data whose range will be chosen as original scale)     

X_scaled = mms.scale(X)                                         #scaling the features of X through use of scale() method

X_revert = mms.revert(X_scaled)                                 #reverting the scaled data back into original scale    



print(X)
print("\n ================================\n")
print(X_scaled)
print("\n ================================\n")
print(X_revert)


# above code displays the output as :

  --------------------   
 |  original datatset |
 |                    |  
 |  ================= |
 |                    |
 |  scaled dataset    |
 |                    |
 |  ================= |
 |                    |
 |  reverted dataset  |
  -------------------- 


"""

