from sklearn.mixture import GaussianMixture
from sklearn.datasets import make_blobs

X, _ = make_blobs(n_samples=200, centers=3, random_state=42)

model = GaussianMixture(n_components=3)
model.fit(X)

labels = model.predict(X)

print("Cluster Labels:", labels[:10])
