#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 20:42:03 2021

@author: janjacob
"""

import pandas as pd
import seaborn as sns

df=pd.read_csv("grad_admissions.csv")

##K means clusters

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

###using the elbow plot you can see 4 clusters

km3 = KMeans(n_clusters=4)##initialize
km3.fit(scaled_df)##training/finding the clusters

df["labels"] = km3.labels_

cluster0 = df.loc[df["labels"] == 0].describe()
cluster1 = df.loc[df["labels"] == 1].describe()
cluster2 = df.loc[df["labels"] == 2].describe()
cluster3 = df.loc[df["labels"] == 3].describe()

## Cluster 0: High GRE score, high TOEFL score, high university ratio, high SOP,
## high LOR, high CGPA, did research
## Cluster 1: Low GRE score, low TOEFL score, low university ratio, low SOP,
## low LOR, low CGPA, no research
## Cluster 2: Medium GRE score, medium TOEFL score, medium university ratio, medium SOP,
## medium LOR, medium CGPA, with research
## Cluster 3: Medium GRE score, medium TOEFL score, medium university ratio, medium SOP,
## medium LOR, medium CGPA, no research

## Hierarchical clustering
df=pd.read_csv("grad_admissions.csv")

from sklearn.preprocessing import MinMaxScaler#import
scaler = MinMaxScaler()#fit/train
scaler.fit(df)#fit/train
scaled_df=scaler.transform(df)

from scipy.cluster.hierarchy import dendrogram,linkage#import
import matplotlib.pyplot as plt
linked = linkage(scaled_df,method="ward")#huge matrix(single,complete,average)
dendrogram(linked)#plot the dendrogram
plt.show()

from sklearn.cluster import AgglomerativeClustering#import
hc=AgglomerativeClustering(n_clusters=4,linkage="ward")#initialize
hc.fit(scaled_df)#train/finding clusters

##add labels to the df
df["labels"]=hc.labels_

# step 4: interpret your clusters
cluster0 = df.loc[df["labels"] == 0].describe()
cluster1 = df.loc[df["labels"] == 1].describe()
cluster2 = df.loc[df["labels"] == 2].describe()
cluster3 = df.loc[df["labels"] == 3].describe()

## Cluster 0: High GRE score, high TOEFL score, high university ratio, high SOP,
## high LOR, high CGPA, did research
## Cluster 1: Low GRE score, low TOEFL score, low university ratio, low SOP,
## low LOR, low CGPA, low research
## Cluster 2: Medium GRE score, medium/low TOEFL score, medium/low university ratio, medium/low SOP,
## medium/low LOR, medium/low CGPA, with research
## Cluster 3: Medium GRE score, medium/high TOEFL score, medium/high university ratio, medium/high SOP,
## medium/high LOR, medium/high CGPA, no research