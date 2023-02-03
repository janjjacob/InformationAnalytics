#please show your work in a word document. Submit both the .py file and the word document.

#1. #Fit a linear regression model on data: USA_housing.csv to predict the Price of the house.
#Do a simple linear regression and report the RMSE, then see if the model can be improved by adding other variables.
#You may drop the columns that you feel may not be relevant.


"""Data description"""
#Income: Avg. area income
#Age: Avg age of the houses
#Bedrooms: Avg No of bedrooms
#Rooms: Avg No of rooms
#Population: Population of the area
#Price: Average price in the area
#Address: THink of them as different ZIPcodes

import pandas as pd
import seaborn as sns

df=pd.read_csv("USA_housing.csv")

df.info()

corr = df.corr()

x=df[["Avg. Area Income"]]
y=df["Price"]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=1)

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(x_train, y_train)

lr.coef_
lr.intercept_
### Price = -209867 + (Avg. Area Income) * 21.0306331

y_pred = lr.predict(x_test)

from sklearn.metrics import mean_squared_error
mse=mean_squared_error(y_test,y_pred)
rmse=mse**0.5
print("rmse is",rmse) # 269033.18772319076

## MULTIPLE LINEAR REGRESSION
x=df.drop(columns=['Price','Address'])
y=df["Price"]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=1)

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(x_train, y_train)

lr.coef_
lr.intercept_
### Price = -2645289 + (Avg. Area Income) * 2.16398550e+01
### + (Avg. Area House Age) * 1.65729214e+05 + (Avg. Area Number of Rooms) * 1.20958349e+05
### + (Avg. Area Number of Bedrooms) * 1.94909254e+03 + (Area Population) * 1.52262240e+01

y_pred = lr.predict(x_test)

from sklearn.metrics import mean_squared_error
mse=mean_squared_error(y_test,y_pred)
rmse=mse**0.5
print("rmse is",rmse) ## 102798.09614448597




















