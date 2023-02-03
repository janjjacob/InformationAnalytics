#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 08:08:55 2021

@author: janjacob
"""


'''Type 1'''

print("Hola!")
print("Como estas")

def hola():
    print("Hola!")
    print("Como estas")
    
hola()

pp = hola()
print(hola)

def hola(my_name):
    print("Hola!", my_name)
    print("Como estas")

hola("Jan")

'''Type 2'''
def even_or_odd(a):
    if a%2 == 0:
        return "even"
    else:
        return "odd"

even_or_odd(11)

even_or_odd(22)

ppp=even_or_odd(22)
print(ppp)

###functions with dataframe
import pandas as pd
df = pd.read_excel("testing.xlsx")

df["status"]=df["y"].apply(even_or_odd)

###removing on to re library
import re

a_string='abc xxx abc yyy12345!!@@'

re.sub("a", "Python", a_string)

re.sub("1", "Python", a_string)

re.sub("[0-9]", "Python", a_string)

re.sub("\w", "Python", a_string)

re.sub("\s", "Python", a_string)

s="string. 99With. Punctuations?"
##remove numbers
##remove punctuations
##make everything lower case

##data cleaning steps
s=re.sub("[^\w\s]", "", s)
s=re.sub("[0-9]", "", s)
s=s.lower()

##splitting step
s=s.split()

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

###want to create a barplot for words
##ignore the stopwords
from stop_words import get_stop_words
my_list=get_stop_words("english")

word_list=[]

for i in df["splitted_data"]:
    for j in i:
        if j not in my_list:
            word_list.append(j)
            
all_words_list_df = pd.DataFrame(word_list)
counts=all_words_list_df.value_counts()

counts.head(20).plot(kind="bar")

###word cloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt

bing=" ".join(word_list)
jing=WordCloud(width=1000,height=400,background_color="white").generate(text=bing)
plt.figure(figsize=(20,20))
plt.imshow(jing)

###class exercise for today
##make a barplot with most common words
##make a wordcloud

df=pd.read_csv("musk.csv")

df["clean_message"] = df["tweets"].apply(cleandata)

df["splitted_data"]=df["clean_message"].apply(splitdata)

my_list=get_stop_words("english")

word_list=[]

for i in df["splitted_data"]:
    for j in i:
        if j not in my_list:
            word_list.append(j)
            
all_words_list_df = pd.DataFrame(word_list)
counts=all_words_list_df.value_counts()

counts.head(20).plot(kind="bar")

bing=" ".join(word_list)
jing=WordCloud(width=1000,height=400,background_color="white").generate(text=bing)
plt.figure(figsize=(20,20))
plt.imshow(jing)














