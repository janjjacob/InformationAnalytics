#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 08:11:34 2021

@author: janjacob
"""

## NOTE THIS IS CARS AND POKEMON

import pandas as pd
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)


df = pd.read_csv("cars.csv")

df.describe()

df.info()

df.head()

df_8 = df.head(8)

df.tail(9)

df.columns

df["model"]

df[[ 'model', 'year ']]

df["brand"].unique()

df.loc[1]

df.loc[0:4]

df.loc[df["brand"] == "ford"]

df.loc[df["price"]<=5000]

df.loc[ (df["price"]<=5000) & (df["brand"] == "ford")]

df.sort_values(by="price",ascending=False)

df["age"] = 2021-df["year"]

df["miles/yr"] = df["mileage"]/df["age"]

df=df.drop(columns="country")

df["affordability"] = "affordable"

df.loc[df["price"]>12000,"affordability"] = "expensive"

df[["a","b","c"]] = df["condition"].str.split(' ',expand=True)

df.to_csv("cars_1.csv")

df.to_excel("cars_2.xlsx")

df.groupby("brand").median()["price"]

### Class Exercise
pok = pd.read_csv("pokemon_data-1.csv")

pok.info()
# There are 800 - 414 = 386 null missing values in the Type 2 Column

pok.head(15)

pok.tail(7)

pok.loc[3:7]

pok.describe()
# There are 800 total rows

pok.columns

len(pok["Type 1"].unique())
# There are 18 unique values in Type 1

pok.loc[ (pok["Type 1"] == "Grass") & (pok["HP"] > 100) ]

pok["fast"] = "slow"
pok.loc[ pok["Speed"] > 100, "fast" ] = "fast"