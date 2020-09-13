from sklearn import tree
X=[[0, 0], [1, 1]]
y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)             # 학습시킨다.
print(X)
print(y)

clf.predict([[2, 2]])

clf.predict_proba([[2., 2]])

from sklearn.datasets import load_iris
from sklearn import tree
X, y = load_iris(return_X_y=True)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)              

tree.plot_tree(clf)
y

import graphviz
iris = load_iris()
dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.render("iris")

dot_data = tree.export_graphviz(clf, feature_names=iris.feature_names,
                                class_names=iris.target_names, filled= True, rounded=True, special_characters=True)

graph = graphviz.Source(dot_data)
graph
