#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 08:21:46 2021

@author: janjacob
"""

"""
y_test = [0,1,0,0,1,0]
y_pred = [0,1,1,1,0,0]

from sklearn.metrics import accuracy_score,precision_score,recall_score,confusion_matrix, f1_score

accuracy_score(y_test,y_pred)
precision_score(y_test,y_pred)
recall_score(y_test,y_pred)
f1_score(y_test,y_pred)
confusion_matrix(y_test,y_pred)
"""

import pandas as pd
import seaborn as sns

df=pd.read_csv("titanic_data.csv")

#1 : survivors
#2 : does not survive

###data exploration
df.info()
df=df.drop(columns=["PassengerId","Name","Ticket","Cabin"])

##dropping rows with missing values
df=df.dropna()

###creating dummy variables for categorical data
df=pd.get_dummies(df,drop_first=True)

###Logistic regrssion 1 variable
## x is fare
## y is whether passenger survived or not
x=df[["Fare"]] ## format has to be dataframe
y=df["Survived"] ## series format

##split data into training and testing data
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)

##import, initialize, train, evaluate
from sklearn.linear_model import LogisticRegression##import
lg=LogisticRegression(solver="liblinear")##initialize
lg.fit(x_train,y_train)

y_pred=lg.predict(x_test)

##compare predicted values with actual values to see how odel does, f1_score

from sklearn.metrics import f1_score
f1_score(y_test,y_pred)## lies between 0-1 (we want a value close to 1)

##can we improve the modell using all x variables?
x=df.drop(columns="Survived") ## format has to be dataframe
y=df["Survived"] ## series format

##split data into training and testing data
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)

##import, initialize, train, evaluate
from sklearn.linear_model import LogisticRegression##import
lg=LogisticRegression(solver="liblinear")##initialize
lg.fit(x_train,y_train)

y_pred=lg.predict(x_test)

##compare predicted values with actual values to see how odel does, f1_score

from sklearn.metrics import f1_score
f1_score(y_test,y_pred)## lies between 0-1 (we want a value close to 1)

##class exercise
df_default=pd.read_csv("default.csv")
df_default.info()# No missing data
df_default=pd.get_dummies(df_default,drop_first=True)##create dummies for default

## Just Balance
x=df_default[["balance"]]
y=df_default["default_Yes"]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)

lg=LogisticRegression(solver="liblinear")
lg.fit(x_train,y_train)

y_pred=lg.predict(x_test)

f1_score(y_test,y_pred) # 0.9174311926605505 (very good predictor)

##all variables
x=df_default.drop(columns="default_Yes")
y=df_default["default_Yes"]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)

lg=LogisticRegression(solver="liblinear")
lg.fit(x_train,y_train)

y_pred=lg.predict(x_test)

f1_score(y_test,y_pred) # 0.8858447488584476 (very good but not quite as good as just balance)




























