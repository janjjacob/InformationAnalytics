#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 22:55:20 2021

@author: janjacob
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("NYPD_Arrests_Data__Historic_.csv")

df=df.dropna(subset=['AGE_GROUP'])

df = df.loc[(df["AGE_GROUP"] == "<18") | (df["AGE_GROUP"] == "18-24") | (df["AGE_GROUP"] == "25-44") | (df["AGE_GROUP"] == "45-64") | (df["AGE_GROUP"] == "65+")]

sns.countplot(x="AGE_GROUP",data=df,order = df['AGE_GROUP'].value_counts().index)
plt.xlabel("Age Group")
plt.ylabel("Number of Arrests (In Millions)")
plt.title("Number of Arrests by Age Group")
plt.legend()

sns.countplot(x="AGE_GROUP",hue="PERP_SEX",data=df,order = df['AGE_GROUP'].value_counts().index)
plt.xlabel("Age Group")
plt.ylabel("Number of Arrests (In Millions)")
plt.title("Number of Arrests by Age Group and Gender")
plt.legend()

##Analysis of Numbers
dfMale = df.loc[df['PERP_SEX'] == "M"]
dfFemale = df.loc[df['PERP_SEX'] == "F"]

## distribution men amongst age groups
dfMale['AGE_GROUP'].value_counts()

## distribution women amongst age groups
dfFemale['AGE_GROUP'].value_counts()

## ratio of men to women for each age group
dfMale['AGE_GROUP'].value_counts() / dfFemale['AGE_GROUP'].value_counts()
