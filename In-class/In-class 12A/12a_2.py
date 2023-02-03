#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 08:45:25 2021

@author: janjacob
"""

import pandas as pd
df=pd.read_csv("clustering_data2.csv")

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

##step 3: do the custering (4 clusters)
from sklearn.cluster import AgglomerativeClustering#import
hc=AgglomerativeClustering(n_clusters=4,linkage="ward")#initialize
hc.fit(scaled_df)#train/finding clusters

hc.labels_
##add labels to the df
df["labels"]=hc.labels_

# step 4: interpret your clusters
df.groupby(by="labels").mean()
import seaborn as sns
sns.pairplot(df,hue="labels")

####two datasets
# food.csv
# foodprices.xlsx

##hierarchical clustering and identify clusters
##interpret the clusters

#food.csv
df=pd.read_csv("food.csv")

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
hc=AgglomerativeClustering(n_clusters=3,linkage="ward")#initialize
hc.fit(scaled_df)#train/finding clusters

hc.labels_
##add labels to the df
df["labels"]=hc.labels_

# step 4: interpret your clusters
df.groupby(by="labels").mean()
import seaborn as sns
sns.pairplot(df,hue="labels",palette="Set1")

## Cluster 1: medium calories, high protein, medium fat, medium calcium, low iron
## Cluster 2: low calories, low protien, low fat, high calcium, high iron
## Cluster 3: high calories, medium protein, high fat, low calcium, medium iron

#foodprices.xlsx
df=pd.read_excel("foodprices.xlsx")

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
hc=AgglomerativeClustering(n_clusters=3,linkage="ward")#initialize
hc.fit(scaled_df)#train/finding clusters

hc.labels_
##add labels to the df
df["labels"]=hc.labels_

# step 4: interpret your clusters
df.groupby(by="labels").mean()
import seaborn as sns
sns.pairplot(df,hue="labels",palette="Set1")

## Cluster 1: low bread price, low hamburger price, low butter price, medium apples price, low tomatoes price
## Cluster 2: high bread price, high hamburger price, hugh butter price, high apples price, medium tomatoes price
## Cluster 3: medium bread price, medium hamburger price, medium butter price, low apples price, high tomatoes price



