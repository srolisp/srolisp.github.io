from sklearn.datasets import load_iris

import pandas as pd

iris = load_iris()

print(iris)

print(iris.keys())

print(iris.DESCR)

print(iris.feature_names)

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df

df['target'] = iris.target
df['target']

df.head()

df.tail()

df.shape

df.describe()

df.iloc[:,-1].value_counts()

df.target.value_counts()

X_data = iris.data

y_data = iris.target

X_data

y_data
