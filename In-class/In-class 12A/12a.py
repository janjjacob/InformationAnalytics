#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 08:29:11 2021

@author: janjacob
"""

import pandas as pd
df=pd.read_csv("clustering_data1.csv")

# step 1: scale the data (import, initialize, fit, transform)
from sklearn.preprocessing import MinMaxScaler#import
scaler = MinMaxScaler()#fit/train
scaler.fit(df)#fit/train
scaled_df=scaler.transform(df)

# step 2: getting the dendrogram
from scipy.cluster.hierarchy import dendrogram,linkage#import
import matplotlib.pyplot as plt
linked = linkage(scaled_df,method="ward")#huge matrix(single,complete,average)
dendrogram(linked)#plot the dendrogram
plt.show()

##step 3: do the clustering (3 clusters)
from sklearn.cluster import AgglomerativeClustering#import
hc=AgglomerativeClustering(n_clusters=3,linkage="ward")#initialize
hc.fit(scaled_df)#train/finding clusters

hc.labels_
##add labels to the df
df["labels"]=hc.labels_

import seaborn as sns
sns.scatterplot(x="Income",y="Spend",data=df,hue="labels")



