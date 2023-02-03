#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 10:46:28 2021

@author: janjacob
"""

import pandas as pd

df = pd.read_excel("NYPD Arrest Data Cleaned.xlsx")

df["BoroughName"] = "Bronx"

df.loc[df["ARREST_BORO"] == "Q", "BoroughName"]="Queens"
df.loc[df["ARREST_BORO"] == "K", "BoroughName"]="Brooklyn"
df.loc[df["ARREST_BORO"] == "M", "BoroughName"]="Manhattan"
df.loc[df["ARREST_BORO"] == "S", "BoroughName"]="Staten Island"

df.to_excel("NYPD Arrest Data Cleaned With Borough Names.xlsx")
