# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 12:06:38 2020

@author: Azra
"""
#importing the libraries
import pandas as pd
import matplotlib.pyplot as plt
#reading the data from your file
data = pd.read_csv('Advertising.csv')
print(data)
data.head()
#to visualise data
fig , axs = plt.subplots(1,3,sharey = True)
data.plot(kind = 'scatter',x='TV',y='Sales',ax=axs[0],figsize = (14,7))
data.plot(kind = 'scatter',x='Radio',y='Sales',ax=axs[1])

data.plot(kind = 'scatter',x='Newspaper',y='Sales',ax=axs[2])

data.shape

#create Xandy
feature_cols=['Newspaper']
x = data[feature_cols]
y = data.Sales

feature_cols=['TV']
x = data[feature_cols]
y = data.Sales

#follow the usally sklearn pattern: import,instantiate,fit
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x,y)

#print intercet and coefficients
print(lr.intercept_)
print(lr.coef_)

y = a+bx
result = 6.97 + 0.0554*50
print(result)
X_new = pd.DataFrame({'Newspaper':[50]})
X_new.head()

#creating a dataframe with min ad max values of the table
X_new = pd.DataFrame({'TV':[data.TV.min(),data.TV.max()]})
X_new.head()

preds = lr.predict(X_new)
preds

data.plot(kind = 'scatter',x='TV',y='Sales')
plt.plot(X_new,preds,c='red',linewidth = 5)

import statsmodels.formula.api as smf
lr = smf.ols(formula = 'Sales ~ TV',data = data).fit()
lr.conf_int()

#finding the probabity values
lr.pvalues

#finding the r-squared values
lr.rsquared

#multti linear regression
feature_cols = ['TV','Radio','Newspaper']
X = data[feature_cols]
y = data.Sales

lr = LinearRegression()
lr.fit(X,y)

print(lr.intercept_)
print(lr.coef_)

lm = smf.ols(formula='Sales ~TV+Radio+Newspaper',data=data).fit()
lm.conf_int()
lm.summary()

lm = smf.ols(formula='Sales ~TV+Radio',data=data).fit()
lm.conf_int()
lm.summary()
































