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

class Neuron:

    def __init__(self):
        self.w = 1.0     # 가중치를 초기화합니다
        self.b = 1.0     # 절편을 초기화합니다

    def forpass(self, x):
        y_hat = x * self.w + self.b       # 직선 방정식을 계산합니다
        return y_hat

    def backprop(self, x, err):
        w_grad = x * err    # 가중치에 대한 그래디언트를 계산합니다
        b_grad = 1 * err    # 절편에 대한 그래디언트를 계산합니다
        return w_grad, b_grad

    def fit(self, x, y, epochs=100):
        for i in range(epochs):           # 에포크만큼 반복합니다
            for x_i, y_i in zip(x, y):    # 모든 샘플에 대해 반복합니다
                y_hat = self.forpass(x_i) # 정방향 계산
                err = -(y_i - y_hat)      # 오차 계산
                w_grad, b_grad = self.backprop(x_i, err)  # 역방향 계산
                self.w -= w_grad          # 가중치 업데이트
                self.b -= b_grad          # 절편 업데이트
            if (i % 2 == 0):
                plt.scatter(x, [self.forpass(x_i) for x_i in x])

x = diabetes.data[:, 2]
y = diabetes.target

plt.scatter(x, y)
neuron = Neuron()
neuron.fit(x, y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

class Neuron2:

    def __init__(self):
        self.w = 1.0     # 가중치를 초기화합니다
        self.b = 1.0     # 절편을 초기화합니다

    def forpass(self, x):
        y_hat = x * self.w + self.b       # 직선 방정식을 계산합니다
        return y_hat

    def backprop(self, x, err):
        w_grad = x * err    # 가중치에 대한 그래디언트를 계산합니다
        b_grad = 1 * err    # 절편에 대한 그래디언트를 계산합니다
        return w_grad, b_grad

    def fit(self, x, y, epochs=1000):
        for i in range(epochs):           # 에포크만큼 반복합니다
            w_grad = 0
            b_grad = 0
            for x_i, y_i in zip(x, y):    # 모든 샘플에 대해 반복합니다
                y_hat = self.forpass(x_i) # 정방향 계산
                err = -(y_i - y_hat)      # 오차 계산
                w_grad_seg, b_grad_seg = self.backprop(x_i, err)  # 역방향 계산
                # w_grad, b_grad = self.backprop(x_i, err)  # 역방향 계산

                # self.w -= w_grad  
                # self.b -= b_grad
                w_grad += w_grad_seg 
                b_grad += b_grad_seg
            w_grad = w_grad / len(x)
            b_grad = b_grad / len(x)
            self.w -= w_grad          # 가중치 업데이트
            self.b -= b_grad          # 절편 업데이트

            if (i % 2 == 0):
                plt.scatter(x, [self.forpass(x_i) for x_i in x])

plt.scatter(x, y)
neuron2.fit(x, y)
plt.show()

y2 = y.copy()
  y2[-1] = 500
print(y2[-1])

plt.scatter(x, y2)
neuron = Neuron()
neuron.fit(x, y2)
plt.show()

plt.scatter(x, y2)
neuron2.fit(x, y2)
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














