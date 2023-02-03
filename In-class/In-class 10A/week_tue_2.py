#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 08:33:29 2021

@author: janjacob
"""

import pandas as pd
df=pd.read_csv("USA_Housing-1.csv")

###x varialbes : everything except price
###y variables: price

import seaborn as sns
sns.pairplot(df)

cm=df.corr()
sns.heatmap(cm)

'''simple linear regression'''

y=df["Price"]
x=df[['Avg. Area Income']]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=1)

###Now building the model
#1. import
#2. initialize: tell python this is model to be used
#3. train: calculate the regression equation
#4. evaluate: evaluate on test set

from sklearn.linear_model import LinearRegression # import
lr=LinearRegression() # initialize, model is not trained yet
lr.fit(x_train, y_train) # train the model

###get the model parameters
lr.coef_
lr.intercept_
### Price = -209867 + (Total avg income) * 21.03

y_pred = lr.predict(x_test)
#y_pred is predicate values
#y_test is actual values
#to evaluate compare y_pred with y_test

from sklearn.metrics import mean_squared_error
mse=mean_squared_error(y_test,y_pred)
rmse=mse**0.5
print("rmse is",rmse)

'''Multiple linear regression'''

###now x would be everythin except price and address
x=df.drop(columns=['Price','Address'])
y=df['Price']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=1)

from sklearn.linear_model import LinearRegression # import
lr=LinearRegression() # initialize, model is not trained yet
lr.fit(x_train, y_train) # train the model

###get the model parameters
lr.coef_
lr.intercept_
### Price = -209867 + (Total avg income) * 21.03

y_pred = lr.predict(x_test)
#y_pred is predicate values
#y_test is actual values
#to evaluate compare y_pred with y_test

from sklearn.metrics import mean_squared_error
mse=mean_squared_error(y_test,y_pred)
rmse=mse**0.5
print("rmse is",rmse)

## baseball data
#1. develop a simple reg model (based on highest correlation)
#2. multiple linear reg model (see if model improves)
#y is salary
#x is hits and years
dfbb = pd.read_csv("baseball.csv")
cmb = dfbb.corr()

'''Simple reg model'''

y=dfbb["Salary"]
x=dfbb[['Hits']]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=1)

lr=LinearRegression() # initialize, model is not trained yet
lr.fit(x_train, y_train) # train the model

###get the model parameters
lr.coef_
lr.intercept_
### Price = -209867 + (Total avg income) * 21.03

y_pred = lr.predict(x_test)

from sklearn.metrics import mean_squared_error
mse=mean_squared_error(y_test,y_pred)
rmse=mse**0.5
print("rmse is",rmse) # 451.81875606269875

'''Multiple reg model'''
y=dfbb["Salary"]
x=dfbb[['Hits','Years']]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=1)

lr=LinearRegression() # initialize, model is not trained yet
lr.fit(x_train, y_train) # train the model

###get the model parameters
lr.coef_
lr.intercept_
### Price = -209867 + (Total avg income) * 21.03

y_pred = lr.predict(x_test)

from sklearn.metrics import mean_squared_error
mse=mean_squared_error(y_test,y_pred)
rmse=mse**0.5
print("rmse is",rmse) # 430.32571988482607

## model does improve using multiple regression model
