# -*- coding: utf-8 -*-
"""knn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HnmiFtzCduPqF4JLx65xS3n66KmeMQ9F
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("/content/Classified Data")
df

df.head()

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

scaler.fit(df.drop('TARGET CLASS',axis=1))

scaled_features = scaler.transform(df.drop('TARGET CLASS',axis=1))
scaled_features

df_feat = pd.DataFrame(scaled_features,columns=df.columns[:-1])

# df.columns

df_feat.head()

from sklearn.model_selection import train_test_split

X= scaled_features
y=df['TARGET CLASS']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=101)

from sklearn.neighbors import KNeighborsClassifier

knn =KNeighborsClassifier(n_neighbors=1)

knn.fit(X_train,y_train)

pred= knn.predict(X_test)

pred

from sklearn.metrics import classification_report,confusion_matrix

print(confusion_matrix(y_test,pred))
print(classification_report(y_test,pred))

error_rate = []

for i in range(1,35):
  knn = KNeighborsClassifier(n_neighbors=i)
  knn.fit(X_train,y_train)
  pred_i= knn.predict(X_test)
  error_rate.append(np.mean(pred_i != y_test))

plt.figure(figsize=(10,6))
plt.plot(range(1,35),error_rate)



