import numpy as np

X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

y = np.array([[0],
              [1],
              [1],
              [0]])

np.random.seed(1)

W1 = np.random.rand(2, 2)
W2 = np.random.rand(2, 1)

lr = 0.1

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

for epoch in range(10000):
    # Forward pass
    h = sigmoid(np.dot(X, W1))
    out = sigmoid(np.dot(h, W2))

    # Backpropagation
    error = y - out
    d_out = error * sigmoid_derivative(out)
    d_h = d_out.dot(W2.T) * sigmoid_derivative(h)

    # Weight updates
    W2 += h.T.dot(d_out) * lr
    W1 += X.T.dot(d_h) * lr

print("Output after training:\n", out)
