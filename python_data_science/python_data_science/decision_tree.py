# -*- coding: utf-8 -*-
"""decision_tree.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pWOyJM-2CQ--l9Uo6FPJ8Fi1l9IC9HqT
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris

iris=load_iris()
iris
# iris.info()

iris.data

iris.target

df=sns.load_dataset("iris")
df

df.info()

#indepedent and dependent features
X=df[['sepal_length','sepal_width','petal_length','petal_width']]
X
# y=iris.target
# y

y=iris.target
y

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

X_train

from sklearn.tree import DecisionTreeClassifier

tree_model=DecisionTreeClassifier()

tree_model.fit(X_train,y_train)

from sklearn.tree import plot_tree
from sklearn import tree

plt.figure(figsize = (15,10))
tree.plot_tree(tree_model,filled=True)

#prediction
y_pred=tree_model.predict(X_test)

y_pred

from sklearn.metrics import accuracy_score,classification_report

score=accuracy_score(y_pred,y_test)
score

score2=classification_report(y_pred,y_test)
score2

