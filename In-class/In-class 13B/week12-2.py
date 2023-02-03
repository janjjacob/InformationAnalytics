#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 08:19:12 2021

@author: janjacob
"""

import pandas as pd

import re

def cleandata(s):
    s=re.sub("[^\w\s]", "", s)
    s=re.sub("[0-9]", "", s)
    s=s.lower()
    return s

def splitdata(s):
    s=s.split()
    return s

cleandata("string. 99With. Punctuations?")

df=pd.read_excel("messages.xlsx")

df["clean_message"] = df["message"].apply(cleandata)

df["splitted_data"]=df["clean_message"].apply(splitdata)

##textblob exercise starts here!!
from textblob import TextBlob
TextBlob("good").sentiment

#just polarity
TextBlob("not good").sentiment.polarity

#just subjectivity
TextBlob("not good").sentiment.subjectivity

##function for polarity
def polarity_calc(text):
    return TextBlob(text).sentiment.polarity
    
##function for subjectivity
def subject_calc(text):
    return TextBlob(text).sentiment.subjectivity
    
df["polarity"] = df["clean_message"].apply(polarity_calc)
df["subjectivity"] = df["clean_message"].apply(subject_calc)

###plot the polarity and subjectivity
import matplotlib.pyplot as plt
plt.hist(df["polarity"],label="polarity")
plt.hist(df["subjectivity"],label="subjectivity")
plt.legend()

##mostly a positive tone to the conversation

####class exercise: musk.csv (tweets from elon musk)
##create polarity/subjectivity plot for that
##comment on polarity/subjectivity
df=pd.read_csv("musk.csv")

df["clean_message"] = df["tweets"].apply(cleandata)

df["splitted_data"]=df["clean_message"].apply(splitdata)

df["polarity"] = df["clean_message"].apply(polarity_calc)
df["subjectivity"] = df["clean_message"].apply(subject_calc)

plt.hist(df["polarity"],label="polarity")
plt.hist(df["subjectivity"],label="subjectivity")
plt.legend()

## this set of tweets had a somewhat neutral (slightly negative) polarity as 60% of the data was slightly below 0.0
## this set of tweets had a generally positive subjectivity (most just slightly over 0.0)
