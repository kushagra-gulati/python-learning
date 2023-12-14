# -*- coding: utf-8 -*-
"""exploratory_data_analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XdoCarQ31yWSOeBYzrRrXizDTzGMJhDQ

HOME SALES IN KING COUNTRY,USA
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/kc_house_data.csv')

df.head()

df.isnull().sum()

df.describe(include='object')

plt.figure(figsize=(10,7))
sns.displot(df['price'])

#real satte agency model creating
sns.displot(df['bedrooms'])

df.corr()['price'].sort_values()

sns.scatterplot(x='price',y='sqft_living',data=df)

sns.scatterplot(x='price',y='sqft_living15',data=df)

df.columns

sns.scatterplot(x='price',y='long',data=df)

sns.scatterplot(x='price',y='lat',data=df)

sns.scatterplot(x='long',y='lat',data=df,hue='price')

df.sort_values('price',ascending=False).head(20)

length=len(df)
length

non_top_1percent = df.sort_values('price',ascending=False).iloc[216:]

non_top_1percent

sns.scatterplot(x='long',y='lat',data=non_top_1percent,hue='price')

# sns.scatterplot(x='long',y='lat',data=df,hue='price')

# df.head()

df = df.drop('id',axis=1)

df['date'] = pd.to_datetime(df['date'])

df['date']

df['year']= df['date'].apply(lambda date: date.year)
df['month']= df['date'].apply(lambda date: date.month)

df.head()

sns.boxplot(x='month',y='price',data=df)

df.groupby('year').mean()['price'].plot()

df =df.drop('date',axis=1)

df.head()

df =df.drop('zipcode',axis=1)

df['yr_renovated'].value_counts()

X=df.drop('price',axis=1)
y = df['price'].values

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=101)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()

model.add(Dense(19,activation='relu'))
model.add(Dense(19,activation='relu'))
model.add(Dense(19,activation='relu'))
model.add(Dense(19,activation='relu'))

model.add(Dense(1))
model.compile(optimizer = 'adam',loss='mse')

model.fit(x=X_train,y=y_train,validation_data=(X_test,y_test),batch_size=128,epochs=400)

