import pandas as pd
df_train = pd.read_excel('data/titanic3.xls')

# 나이 컬럼 값이 널인경우 전체 나이의 평균으로 할당한다
df_train['age'] = df_train['age'].fillna(df_train['age'].mean())

df_train.drop(['cabin'], axis='columns', inplace=True)
df_train.drop(['embarked'], axis='columns', inplace=True)
df_train.drop(['boat'], axis='columns', inplace=True)
df_train.drop(['name'], axis='columns', inplace=True)
df_train.drop(['ticket'], axis='columns', inplace=True)
df_train.drop(['body'], axis='columns', inplace=True)
df_train.drop(['home.dest'], axis='columns', inplace=True)

df_train['fare'] = df_train['fare'].fillna(0)

# sex 컬럼을 범주형에서 수치형으로 변환한다.
df_train['sex'] = df_train['sex'].map({'female':0, 'male':1})

df_train.info()

df_X = df_train[['pclass', 'sex','age','sibsp', 'parch', 'fare']]
df_y = df_train[['survived']]

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
# test_size 90:10 의 비율로 train과test로 나눈다.
X_train, X_test, y_train, y_test = train_test_split(df_X, df_y, test_size=0.1, random_state=0 )

from sklearn.tree import DecisionTreeClassifier

tree = DecisionTreeClassifier(max_depth=4, random_state=3)
tree.fit(X_train, y_train)
print('점수는 '+ str(tree.score(X_train, y_train)))

y_pred = tree.predict(X_test)
print('정확도는', accuracy_score(y_test, y_pred) * 100)

# ['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare']
winslet = [1, 0, 17, 1, 2, 100]
dicaprio = [3, 1, 19, 0, 0, 5]

print('윈슬렛')
if tree.predict([winslet])[0] == 0:
  print('사망', '--->', max(tree.predict_proba([winslet])[0]))
else:
  print('생존', '--->', max(tree.predict_proba([winslet])[0]))
print('디카프리오')
if tree.predict([dicaprio])[0] == 0:
  print('사망', '--->', max(tree.predict_proba([dicaprio])[0]))
else:
  print('사망', '--->', max(tree.predict_proba([dicaprio])[0]))

from sklearn.tree import export_graphviz

export_graphviz(
  tree,
  out_file='titanic.dot',
  feature_names=['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare'],
  class_names=['Unsurvived', 'Survived'],
  filled=True,
  rounded=True
  )

import graphviz
with open('titanic.dot') as f: 
  dot_graph = f.read()
dot = graphviz.Source(dot_graph)
dot.format='png'
dot.render(filename='titanic_tree', directory='dicision_tree', cleanup=True)
dot

import matplotlib.pyplot as plt
training_accuracy = []
test_accuracy = []

depth_settings = range(1, 31)

for depth in depth_settings:
  tree = DecisionTreeClassifier(max_depth=depth, random_state=3)
  tree.fit(X_train, y_train)

  training_accuracy.append(tree.score(X_train, y_train))
  test_accuracy.append(tree.score(X_test, y_test))

plt.figure(figsize=[20,10])
plt.plot(depth_settings, training_accuracy, label="training_accuracy")
plt.plot(depth_settings, test_accuracy, label="test_accuracy")
plt.xlabel("depth")
plt.ylabel("accuracy")
plt.legend()

from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier()

clf.fit(X_train, y_train)

print('점수는 '+ str(tree.score(X_train, y_train)))

y_pred = tree.predict(X_test)
print('정확도는', accuracy_score(y_test, y_pred) * 100)

print('윈슬렛')
if clf.predict([winslet])[0] == 0:
  print('사망', '--->', max(clf.predict_proba([winslet])[0]))
else:
  print('생존', '--->', max(clf.predict_proba([winslet])[0]))

  print('디카프리오')
if clf.predict([dicaprio])[0] == 0:
  print('사망', '--->', max(clf.predict_proba([dicaprio])[0]))
else:
  print('생존', '--->', max(clf.predict_proba([dicaprio])[0]))
