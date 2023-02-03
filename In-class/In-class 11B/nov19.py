#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 08:31:09 2021

@author: janjacob
"""

import pandas as pd
import seaborn as sns
df = pd.read_csv("clustering_data1.csv")

###step 1: scale the data
# imports, initialize, traing, transform
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

km3 = KMeans(n_clusters=3)##initialize
km3.fit(scaled_df)##training/finding the clusters

##which observations go to which clusters
km3.labels_

df["labels"] = km3.labels_

sns.scatterplot(x="Income",y="Spend",data=df,hue="labels",palette="Set1")

##interpret the clusters
# cluster 0: low income, low spending
# cluster 1: high income, high spending
# cluster 2: medium income and medium spending group

## clustering_data2
import pandas as pd
import seaborn as sns
df = pd.read_csv("clustering_data2.csv")

###step 1: scale the data
# imports, initialize, traing, transform
from sklearn.preprocessing import MinMaxScaler##import
scaler = MinMaxScaler()#initializer
scaler.fit(df)#train
scaled_df = scaler.transform(df)#actual transform happens 

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

###using the elbow plot you can see 4 clusters


km4 = KMeans(n_clusters=4)##initialize
km4.fit(scaled_df)##training/finding the clusters

##which observations go to which clusters
km4.labels_

df["labels"] = km4.labels_

##interpret the clusters(using pandas)

df.loc[df["labels"] == 0].describe()
df.loc[df["labels"] == 1].describe()
df.loc[df["labels"] == 2].describe()
df.loc[df["labels"] == 3].describe()

## cluster 0: medium income and spend, early 30s
## cluster 1: high income and spend, 55-60
## cluster 2: low income and spend, young people
## cluster 3: medium income and spend, middle age people


### CLASS EXERCISE
df=pd.read_csv("future-1.csv")

###step 1: scale the data
# imports, initialize, traing, transform
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

km3 = KMeans(n_clusters=3)##initialize
km3.fit(scaled_df)##training/finding the clusters

##which observations go to which clusters
km3.labels_

df["labels"] = km3.labels_

sns.scatterplot(x="INCOME",y="SPEND",data=df,hue="labels",palette="Set1")

## cluster 0 : medium spending high income
## cluster 1: low income, high spending
## cluster 2: low income low spending









