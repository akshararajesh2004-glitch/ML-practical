import numpy as np
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)

# Population of binary feature masks
population = np.random.randint(0, 2, size=(6, X.shape[1]))

def fitness(mask):
    if np.sum(mask) == 0:
        return 0

    X_sel = X[:, mask == 1]

    X_train, X_test, y_train, y_test = train_test_split(
        X_sel, y, test_size=0.3, random_state=42
    )

    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    return accuracy_score(y_test, model.predict(X_test))

scores = [fitness(ind) for ind in population]
best = population[np.argmax(scores)]

print("Best Feature Mask:", best)
