#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 10:20:02 2021

@author: janjacob
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("NYPD Arrest Data Cleaned.xlsx")

df["Male"] = 1
df.loc[df["PERP_SEX"] == "F", "Male"]=0

## 0 - <18
## 1 - 18-24
## 2 - 25-44
## 3 - 45-64
## 4 - 65+
df["Age_Groups"] = 0

df.loc[df["AGE_GROUP"] == "18-24", "Age_Groups"]=1
df.loc[df["AGE_GROUP"] == "25-44", "Age_Groups"]=2
df.loc[df["AGE_GROUP"] == "45-64", "Age_Groups"]=3
df.loc[df["AGE_GROUP"] == "65+", "Age_Groups"]=4

## 0 - black
## 1 - white
## 2 - ASIAN / PACIFIC ISLANDER
## 3 - black hispanic / white hispanic
## 4 - other
df["ETHNICITY"] = 0

df.loc[df["PERP_RACE"] == "WHITE", "ETHNICITY"]=1
df.loc[df["PERP_RACE"] == "ASIAN / PACIFIC ISLANDER", "ETHNICITY"]=2
df.loc[df["PERP_RACE"] == "BLACK HISPANIC", "ETHNICITY"]=3
df.loc[df["PERP_RACE"] == "WHITE HISPANIC", "ETHNICITY"]=3
df.loc[df["PERP_RACE"] == "OTHER", "ETHNICITY"]=4

## We see no strong correlation between any of the variables
cor = df.corr()

## TRYING CLUSTERING
## FIRST HAVE TO REMOVE CATEGORICAL DATA
df.drop(['PD_DESC', 'ARREST_BORO', 'AGE_GROUP', 'PERP_SEX', 'PERP_RACE', 'OFNS_DESC', 'Unnamed: 9', 'Most Committed Crime'],inplace=True, axis=1)
df=df.dropna()

from sklearn.preprocessing import MinMaxScaler##import
scaler = MinMaxScaler()#initializer
scaler.fit(df)#train
scaled_df = scaler.transform(df)#actual transform happens here

###we will use elbow method to find the number of clusters

from sklearn.cluster import KMeans ##importing
wcv=[]##empty list

for i in range(2,11):
    km = KMeans(n_clusters=i)##initialize
    km.fit(scaled_df)##training/finding the clusters
    wcv.append(km.inertia_)##within cluster variation
    
import matplotlib.pyplot as plt
plt.plot(range(2,11),wcv)
plt.xlabel("K or no of clusters")
plt.ylabel("Within cluster variation")

###using the elbow plot you can see 3 clusters

km3 = KMeans(n_clusters=4)##initialize
km3.fit(scaled_df)##training/finding the clusters

df["labels"] = km3.labels_

## Because we converted categorical variables to dummy variables and are using those,
## the results of clustering do not show anything relevant as we cannot accurately
## depict the ethnicity or age group of the clusters clearly
cluster0 = df.loc[df["labels"] == 0].describe()
cluster1 = df.loc[df["labels"] == 1].describe()
cluster2 = df.loc[df["labels"] == 2].describe()
cluster3 = df.loc[df["labels"] == 3].describe()