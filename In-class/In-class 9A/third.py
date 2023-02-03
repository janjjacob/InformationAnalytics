#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 08:07:51 2021

@author: janjacob
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Revenue_B.xlsx")

plt.figure(figsize=(10,5))
plt.plot(df["Revenue ($)"], label="Label inside", color="red")
plt.xlabel("Time Period", fontsize=16)
plt.ylabel("Revenue", fontsize=20)
plt.legend(fontsize=18)
plt.xticks(fontsize=15, rotation=90)
plt.yticks(fontsize=12, rotation=50)

## getting moving average
df["7 day moving average"]=df["Revenue ($)"].rolling(7).mean()
df["mean revenue"] = df["Revenue ($)"].mean()

df.to_csv("myfile.csv")

plt.plot(df["Revenue ($)"], label="Revenue over time")
plt.plot(df["7 day moving average"], label="7 day moving average")
plt.plot(df["mean revenue"], label="Mean Revenue",linestyle="--")
plt.legend()

# Simple plots

line1 = [20,30,50]
line2 = [4,10,50]

plt.plot(line1)
plt.plot(line2)

plt.plot(line1, line2)
plt.text(25,40,"This is how we write")

plt.scatter(line1,line2,color="red")

## Moving on:airline passanger data

df_air = pd.read_csv("airline_passengers.csv")

plt.plot(df_air["Period"], df_air["Thousands of Passengers"],label="Passangers per Period")

## Can you add 10 period moving average to this plot
## Can you also add the mean line for this plot
df_air["10 day moving average"] = df_air["Thousands of Passengers"].rolling(10).mean()
df_air["mean"] = df_air["Thousands of Passengers"].mean()

plt.plot(df_air["10 day moving average"], label="10 Day Moving Average")
plt.plot(df_air["mean"], label="Mean")
plt.legend()

## cars dataset
df_cars = pd.read_csv("cars.csv")

## histograms: show the distribution of the data
plt.hist(df_cars["price"],bins=20,ec="black",label="price of cars",color="red")
plt.xlabel("price of cars")
plt.ylabel("Frequency")
plt.legend()

##compare the distribution of ford vs dodge
df_cars_ford=df_cars.loc[df_cars["brand"]=="ford"]
df_cars_dodge=df_cars.loc[df_cars["brand"]=="dodge"]

plt.hist(df_cars_ford["price"],bins=20,ec="black",label="Price of ford", alpha=1)
plt.hist(df_cars_dodge["price"],bins=20,ec="black",label="Price of dodge")
plt.legend()

## aggregate data using groupby
mean_cars_by_brand = df_cars.groupby(by="brand").mean()[["price"]]

plt.bar(mean_cars_by_brand.index,mean_cars_by_brand["price"])
plt.xticks(rotation = 90)

mean_cars_by_brand_sorted = mean_cars_by_brand.sort_values(by="price")

plt.bar(mean_cars_by_brand_sorted.index,mean_cars_by_brand_sorted["price"])
plt.xticks(rotation = 90)

## Class exercise
## Can you do a similar plot with mileage instead of price

## Price vs Years Scatterplot
plt.figure(figsize=(10,5))
plt.scatter(df_cars["year"], df_cars["price"])
plt.title("Price vs Year")
plt.xlabel("Years")
plt.ylabel("Price")

## Price vs Mileage Scatterplot
plt.figure(figsize=(10,5))
plt.scatter(df_cars["mileage"], df_cars["price"])
plt.title("Price vs Milage")
plt.xlabel("Mileage")
plt.ylabel("Price")

## Mean Milage Histogram
mean_cars_by_brand = df_cars.groupby(by="brand").mean()[["mileage"]]

mean_cars_by_brand_sorted = mean_cars_by_brand.sort_values(by="mileage")

plt.bar(mean_cars_by_brand_sorted.index,mean_cars_by_brand_sorted["mileage"])
plt.xticks(rotation = 90)
plt.ylabel("Mean Mileage")
