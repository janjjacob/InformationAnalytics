#*****************************************************
#This assignment is to be done using Python
#*****************************************************


"""Refer to the got_battles dataset
#Below are are a series of questions that you need to answer based on visualizations of the data.
 For each one, copy and paste your final code, along with the visualization, and answer to the question into your Word document"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("got_battles.csv")

##are there any missing values?
##If yes, drop the rows that have missing values.
df.info()
# There are missing values
df=df.dropna()


##Which year had the most battles?
sns.countplot(x="year", data=df)
# Year 299 had the most battles (17)

##Which year had the most wins from attackers perspective?
wins=df.loc[df["attacker_outcome"]=="win"]
wins_by_year = wins.groupby('year').count()["name"]
plt.bar(wins_by_year.index,wins_by_year)

# Year 299 had the most wins (14)

##which year had the least battles?
sns.countplot(x="year", data=df)
# Year 298 had the least battles (7)

##Which region had the most battles?
sns.countplot(x="region", data=df)
plt.xticks(rotation=90)
# Riverdale had the most battles (13)

##Which region had least battles?
sns.countplot(x="region", data=df)
plt.xticks(rotation=90)
# Beyond the Wall had the least battles (1)

##What was the outcome of all battles from attacker's perspective?
sns.countplot(x="attacker_outcome", data=df)
# The attackers had 5 losses and 28 wins in total

##How common were different types of battles?
sns.countplot(x="battle_type", data=df)
# ambush - 10, pitched battle - 11, razing - 1, siege - 11

##Which king was the most attacked?
sns.countplot(x="defender_king", data=df)
plt.xticks(rotation=90)
# Joffrey/Tommen Baratheon was attacked the most (12)

##Which king attacked the most?
sns.countplot(x="attacker_king", data=df)
plt.xticks(rotation=90)
# Joffrey/Tommen Baratheon attacked the most (12)

##Which year had highest chances of winning from attacker's perspective?
percent_winning_by_year = wins.groupby('year').count()["name"] / df.groupby("year").count()["name"]
plt.bar(percent_winning_by_year.index,percent_winning_by_year)
plt.xticks(rotation=90)
# year 300 has the highest win percentage of winning

##Compare the mean deaths for different years?
mean_deaths_by_year = df.groupby(by="year").mean()["total deaths"]
plt.bar(mean_deaths_by_year.index,mean_deaths_by_year)
# 300 has the lowest mean with 643.222222, then 298 has a mean of 734.714286, and 299 has a mch higher mean of 1205.176471

##Compare the mean deaths for different battle types?
mean_deaths_by_battle_type = df.groupby(by="battle_type").mean()["total deaths"]
plt.bar(mean_deaths_by_battle_type.index,mean_deaths_by_battle_type)

# pitched battle has the lowest mean of 549.545455, then siege has a mean of 1098.818182,
# then razing has a mean of 1145, and ambush has the highest mean of 1214.3

##Plot the total(sum of) deaths for different battle types?
sns.countplot(x="battle_type", data=df)

##Using visualizations share any three interesting insights (other than the above questions) from this dataset.
tc=df.corr()
sns.heatmap(tc)
## This shows a strong correlation between battle_number and the year

sns.countplot(x="major_death", data=df)
# this shows that more battles did not have a major death (20 compared to 12)

sns.countplot(x="summer", data=df)
# this shows that more battles happened in the summer (24 compared to 8)





