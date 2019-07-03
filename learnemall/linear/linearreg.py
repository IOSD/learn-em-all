#importing libraries

import numpy as np
from linear.datasets.diabetes import load_data



"""
the LinearRegression class contains three methods :

predict() for prediction of outputs
cal_cost() for calculating mean squared error (cost)
fit() for fitting the model by the use of gradient descent algo

"""


class LinearRegression:

    def __init__(self):
        self.theta=0
        self.theta_hist=0
        self.cost_hist=0

    def predict(self,x,theta):
        m=np.shape(x)[0]
        onecol = np.ones([m, 1])
        x = np.hstack((onecol, np.atleast_2d(x)))
        predictions=np.dot(x,theta)
        return predictions


    def cal_cost(self,theta,x,y):
        m = len(y)
        predictions= np.dot(x,theta)
        cost=(1/(2*m))* np.sum(np.square(np.subtract(predictions,y)))
        return cost


    def fit(self,x,y,alpha=0.1,num_iters=1000):
        m = len(y)
        num_features = np.shape(x)[-1]
        onecol = np.ones([m, 1])
        x = np.hstack((onecol, np.atleast_2d(x)))
        y=y.reshape(m,1)
        self.theta = np.zeros([num_features+1, 1])

        self.cost_hist=np.zeros(num_iters)
        self.theta_hist=np.zeros((num_iters,num_features+1))
        print('Running gradient descent .........\n')

        for i in range(num_iters):
            predictions=np.dot(x,self.theta)

            self.theta= self.theta - (1/m)*alpha*(np.dot(x.T,np.subtract(predictions,y)))

            self.theta_hist[i,:]= self.theta.T
            self.cost_hist[i]=LinearRegression().cal_cost(self.theta,x,y)

        print("...Training complete")





"""
X,y = load_data(split=False, ratio = None, path= "./datasets/data/diabetes.csv")

lr=0.01
iters=1000

model=LinearRegression()
model.fit(X,y,lr,iters)
print(model.cost_hist)
print(model.theta_hist)
print(model.theta)


"""
#the above code displays the cost history , theta history and final theta respectively .




