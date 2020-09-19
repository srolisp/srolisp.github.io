from sklearn.datasets import load_diabetes 
diabetes = load_diabetes()

print(diabetes)

print(diabetes.data.shape, diabetes.target.shape)

print(diabetes.data[0:3])

print(diabetes.target[:3])

print(diabetes.data[:, 2])

import matplotlib.pyplot as plt

plt.scatter(diabetes.data[:, 2], diabetes.target)
plt.plot([-0.10, 0.15], [0, 350], 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

x = diabetes.data[:, 2]
y = diabetes.target

w = 1.0
b = 1.0

y_hat = x[0] * w + b
print(y_hat)

print(y[0])

w_inc = w + 0.1
y_hat_inc = w_inc * x[0] + b
print(y_hat_inc)

w_rate = (y_hat_inc - y_hat) / (w_inc - w)
print(w_rate)














