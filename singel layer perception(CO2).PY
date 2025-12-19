import numpy as np

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])

weights = np.zeros(2)
bias = 0
lr = 0.1

def activation(z):
    return 1 if z >= 0 else 0

for epoch in range(10):
    for i in range(len(X)):
        z = np.dot(X[i], weights) + bias
        y_pred = activation(z)
        error = y[i] - y_pred
        weights += lr * error * X[i]
        bias += lr * error

print("Weights:", weights)
print("Bias:", bias)
