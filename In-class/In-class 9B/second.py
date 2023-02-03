#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 08:09:44 2021

@author: janjacob
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("titanic_data.csv")

df.info()

sns.heatmap(df.isnull())

df=df.drop(columns="Cabin")

plt.figure(figsize=(10,10))
sns.histplot(df["Age"],color="red",bins=30)
plt.legend()
plt.xlabel("I can change it")

sns.histplot(df["Fare"])

df_=pd.read_csv("height_gender.csv")

df_male = df_.loc[df_["Gender"] == "Male"]
df_female = df_.loc[df_["Gender"] == "Female"]

sns.histplot(df_male["Height"], color="red", label="Male Height")
sns.histplot(df_female["Height"], color="green", label="Female Height")
plt.legend()

sns.relplot(x="Age",y="Fare",data=df)

sns.relplot(x="Age",y="Fare",data=df,hue="Sex")

sns.relplot(x="Age",y="Fare",data=df,hue="Sex",size="Pclass")

sns.relplot(x="Age",y="Fare",data=df,hue="Sex",size="Survived")

## jointplots
sns.jointplot(x="Age",y="Fare",data=df)

sns.jointplot(x="Age",y="Fare",data=df,kind="reg")

sns.jointplot(x="Age",y="Fare",data=df,kind="hex")

## pairplot
sns.pairplot(df, hue="Sex")

sns.countplot(x="Sex",data=df)

sns.countplot(x="Sex",data=df, hue="Pclass")

####age_category
##teans < 18
## adults (18,60)
## elders (more than 60)

df["age_category"]="teens"

df.loc[(df["Age"]>18) & (df["Age"]<60), "age_category"]="adults"

df.loc[(df["Age"]>60), "age_category"]="elders"

sns.countplot(x="age_category",data=df,hue="Pclass")

tc=df.corr()

sns.heatmap(tc)

##boxplots
df_long=pd.read_excel("format.xlsx",sheet_name="long")
df_wide=pd.read_excel("format.xlsx",sheet_name="wide")

## long format
sns.boxplot(x="Attribute",y="Value",data=df_long)

## wide format
sns.boxplot(data=df_wide)

###boxplot for titanic data
sns.boxplot(x="Sex",y="Age",data=df)

sns.boxplot(x="Pclass",y="Age",data=df)

####In-class exercise

df_cars=pd.read_csv("cars-2.csv")

#1
sns.pairplot(df_cars)

#2
sns.jointplot(x="price",y="mileage",data=df_cars)

#3
cars_corr=df_cars.corr()
sns.heatmap(cars_corr)

#4
plt.figure(figsize=(10,10))
sns.boxplot(x="brand",y="price",data=df_cars)

#5
plt.figure(figsize=(10,10))
sns.countplot(x="brand", data=df_cars)
plt.xticks(rotation=90)

#6
sns.relplot(x="price",y="mileage",data=df_cars,hue="title_status",palette="Set1")








