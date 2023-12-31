# -*- coding: utf-8 -*-
"""keras.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Tx4O9RNWvKg7I1WNdPto5mGWyN0vqTNi
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df =pd.read_csv("/content/fake_reg.csv")

df.head()

sns.pairplot(df)

from sklearn.model_selection import train_test_split

X = df[['feature1','feature2']].values
y = df['price'].values

X

y

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.33,random_state=42)

X_train.shape

X_test.shape

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

scaler.fit(X_train)

X_train=scaler.transform(X_train)

X_test = scaler.transform(X_test)

X_train.min()

X_train.max()

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# none

model = Sequential()
model.add(Dense(4,activation='relu'))
model.add(Dense(4,activation='relu'))
model.add(Dense(4,activation='relu'))
model.add(Dense(1))

model.compile(optimizer='rmsprop', loss='mse')

model.fit(x=X_train,y=y_train,epochs=250)

loss_df = pd.DataFrame(model.history.history)

loss_df.plot()