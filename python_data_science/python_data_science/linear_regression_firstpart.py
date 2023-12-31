# -*- coding: utf-8 -*-
"""linear_regress_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aYx3px4Tfb2jy1egpZ9UFphCYe1qXuAK
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df1=pd.read_csv('/content/USA_Housing.csv')
df1

df1.head()

df1.info()

df1.describe()

sns.heatmap(df1.corr())

df1.columns

X=df1[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population']]

y=df1['Price']

from sklearn.model_selection import train_test_split

train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.4,random_state=101)

from sklearn.linear_model import LinearRegression

lm= LinearRegression()

lm.fit(X_train,y_train)

print(lm.intercept_)

lm.coef_

pd.DataFrame(lm.coef_,X.columns,columns=['Coeff'])

#PREDICTIONS
predictions=lm.predict(X_test)
predictions

plt.scatter(x=y_test,y=predictions,alpha=0.995)

#histogram
sns.histplot(y_test-predictions)
# sns.histplot(y_test+predictions)

#PREDICTIONS start heres
from sklearn import metrics
metrics.mean_absolute_error(y_test,predictions)

metrics.mean_squared_error(y_test,predictions)

np.sqrt(metrics.mean_squared_error(y_test,predictions))





