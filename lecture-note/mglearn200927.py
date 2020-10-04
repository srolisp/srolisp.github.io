import numpy as np
from numpy.linalg import inv
class LogisticRegression:

    def __init__(self, n_iters=1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None
        self.a = None

    def fit(self, X, y):
        # init parameters
        # n_samples, n_features = X.shape
        self.weights = np.zeros(X.shape[1])

        for _ in range(self.n_iters):
            wx = np.dot(X, self.weights)
            a = self._sigmoid(wx)
            one_a = np.array([1-a_i for a_i in a])

            B = np.diag(a * one_a)
            dldw = np.dot((a - y).T, X)
            d2ldw2 = np.dot(np.dot(X.T, B), X)
            inv_d2ldw2 = inv(d2ldw2)
            # update weights
            self.weights -= np.dot(inv_d2ldw2, dldw)
        self.a = a

    def predict(self, X):
        y_predicted = self._sigmoid(np.dot(X, self.weights))
        y_predicted_cls = [1 if i > 0.5 else 0 for i in y_predicted]
        return y_predicted_cls

    def result_a(self):
        return self.a

    def result_weights(self):
        return self.weights

    def _sigmoid(self, a):
         return 1 / (1 + np.exp(-a))

    def _print_debug(self, str, X):
         print(str + '\n', X.shape)
         print(X)

from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt

bc = datasets.load_breast_cancer()
X, y = bc.data[:,:21], bc.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

def accuracy(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy

r = LogisticRegression()
r.fit(X_train, y_train)
predictions = r.predict(X_test)

print("LR classification accuracy:", accuracy(y_test, predictions))

x_3d = np.linspace(0, 40, 455)
# print(len(x_3d))
y_3d = np.linspace(0, 3000, 455)
# print(len(y_3d))
# x_3d, y_3d = np.meshgrid(x_3d, x_3d)
z = r.result_a()
# print(len(z))
fig = plt.figure(figsize=(6,9))
ax = fig.add_subplot(111, projection='3d')
# ax.contour(x_3d, y_3d, z.reshape(35, 13))
# ax.scatter(X_train[:,10],X_train[:,3],r.result_a())
# ax.plot_surface(x_3d,y_3d,z.reshape(13, 35))
ax.scatter(X_train[:,10],X_train[:,3],y_train, marker='.',c='red')
ax.scatter(X_train[:,10],X_train[:,3],z)


# ax.plot(x_3d,y_3d, z )
ax.view_init(elev=5.,
azim=320
)

plt.figure()
plt.scatter(np.dot(X_train, r.result_weights()), r.result_a(), marker='.')
plt.scatter(np.dot(X_train, r.result_weights()), y_train, marker='_', c='red', alpha=.3)
plt.show()
