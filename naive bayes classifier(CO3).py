import numpy as np

X = np.array([[1,1],[1,0],[0,1],[0,0]])
y = np.array(['Yes','Yes','No','No'])
x = np.array([1,1])

classes = np.unique(y)
priors = {c: np.mean(y == c) for c in classes}
likelihood = {c: X[y == c].mean(axis=0) for c in classes}

post = {c: priors[c] * np.prod(likelihood[c]**x * (1-likelihood[c])**(1-x))
        for c in classes}

print("Prediction:", max(post, key=post.get))
