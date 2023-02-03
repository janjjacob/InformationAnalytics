#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 08:21:49 2021

@author: janjacob
"""

import pandas as pd
df = pd.read_csv("train_test-1.csv")

import seaborn as sns
sns.pairplot(df)

y=df["Price"]
x=df[['Bedrooms','Sq.Feet','Neighborhood']]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=1)

#traning_data : x_train, y_train
# test data : x_test,y_test








