import numpy as np

# Sample data
X = np.array([4, 5, 6, 5, 4, 6, 5])

mean_mle = np.mean(X)
var_mle = np.var(X)   # MLE variance (divides by n, not n-1)

print("Estimated Mean:", mean_mle)
print("Estimated Variance:", var_mle)
