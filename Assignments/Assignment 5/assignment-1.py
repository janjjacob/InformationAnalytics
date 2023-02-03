"""Assignment: Use the Titanic data set which is provided.
Please write your code after the comments, and upload the completed .py file along with the excel files.
"""
# survived:	Survival	0 = No, 1 = Yes
# pclass:	Ticket class	1 = 1st, 2 = 2nd, 3 = 3rd
# sex:	Sex	
# Age:	Age in years	
# Siblings/Spouses Aboard': siblings / spouses aboard the Titanic	
# Parents/Children Aboard:	# of parents / children aboard the Titanic	
# fare:	Passenger fare	

'''Part 1'''

import pandas as pd

#Import the data and relevant libraries
df = pd.read_csv("Titanic-2.csv")

##Is there any missing values in the data? If yes, which columns have missing data?
df.info() # THERE IS NO MISSING INFO (there are 887 non-null values in each column)

#sort data based on decreasing "age" and assign it to a variable called age_sorted
age_sorted = df.sort_values(by="Age", ascending=False)

#get all rows for which the "Survived" value is 1, and assign to a variable called survivors.
survivors = df.loc[df["Survived"] == 1]

#get all rows for which the "Survived" value is 0, and assign to a variable called nonsurvivors.
nonsurvivors = df.loc[df["Survived"] == 0]

#get all rows for which "Sex" is male, "Age" is more than 30, and "Fare" is more than 15
df.loc[(df["Sex"] == "male") & (df["Age"] > 30) & (df["Fare"] > 15)]

#How many males were in the first Pclass?
df.loc[(df["Sex"] == "male") & (df["Pclass"] == 1)].info() # 122

#Get the name of the person(s) who paid the highest fare?
df.sort_values(by="Fare", ascending=False).head(1)["Name"]
# Mr. Thomas Drake Martinez Cardeza

#The person who paid the highest fare was in which Pclass?
df.sort_values(by="Fare", ascending=False).head(1)["Pclass"]
# 1

##how many females survived?
df[(df["Sex"] == "female") & (df["Survived"] == 1)].info()
# 233

##How many males survived?
df[(df["Sex"] == "male") & (df["Survived"] == 1)].info()
# 109

#How many females less than 35 years of age survived?
df[(df["Sex"] == "female") & (df["Survived"] == 1) & (df["Age"] < 35)].info()
# 158

#How many males in Pclass 1 paid more than 15$?
df[(df["Sex"] == "male") & (df["Pclass"] == 1) & (df["Fare"] > 15)].info()
# 116

#Get rows 3-9 (including both 3 and 9)
df.loc[3:9]

#get last 10 rows
df.tail(10)

#Passengers in which Pclass (1,2,3) paid the highest mean fare?
df.groupby("Pclass").mean()["Fare"]
# Pclass 1

#Compare the mean fare price of people who survived and who did not.
df.groupby("Survived").mean()["Fare"]
# People who survived had a mean fare price of 48.395 as opposed to 
# people who did not survive who only had a mean of 22.209 (26.186 difference)

#create a new column which is sum of 'Siblings/Spouses Aboard' and 'Parents/Children Aboard'. Name the column appropriately.
df["People Abroad"] = df["Siblings/Spouses Aboard"] + df["Parents/Children Aboard"]

#save the file as an Excel file with name updated_file
df.to_excel("updated_file.xlsx");

'''Part 2'''


#Write a program to print the cube of numbers from 2 to 100 (2 and 100 included)
def cube():
    for i in range(2,101):
        print(i**3)
cube()

#Write a program to print all odd numbers from 2 to 100
def oddNumbers():
    for i in range(2,101):
        if i%2 == 1:
            print(i)
oddNumbers()

#What is a library in python? Name 6 python libraries.
# A library in python is a module of commands or functionality that you can import
# to use in your python program.

# 6 python libraries are pandas, numpy, matplotlib, tensorflow, pytorch, and
# Beautiful Soup


