#Import the libraries required
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the excel data 
dataset = pd.read_excel('D:\MachineLearing\Machine Learning A-Z Template Folder\Part 2 - Regression\Section 4 - Simple Linear Regression\CricketChirpsVs.Temperature.xls')

x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

#Split the data into train and test dataset
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=1/3,random_state=42)

#Fitting Simple Linear regression data model to train data set
from sklearn.linear_model import LinearRegression
regressorObject=LinearRegression()
regressorObject.fit(x_train,y_train)

#predict the test set
y_pred_test_data=regressorObject.predict(x_test)


# Visualising the Training set results in a scatter plot
plt.scatter(x_train, y_train, color = 'red')
plt.plot(x_train, regressorObject.predict(x_train), color = 'blue')
plt.title('Cricket Chirps vs Temperature (Training set)')
plt.xlabel('Cricket Chirps (chirps/sec for the striped ground cricket) ')
plt.ylabel('Temperature (in degrees Fahrenheit)')
plt.show()

# Visualising the test set results in a scatter plot
plt.scatter(x_test, y_test, color = 'red')
plt.plot(x_train, regressorObject.predict(x_train), color = 'blue')
plt.title('Cricket Chirps vs Temperature (Test set)')
plt.xlabel('Cricket Chirps (chirps/sec for the striped ground cricket) ')
plt.ylabel('Temperature (in degrees Fahrenheit)')
plt.show()
