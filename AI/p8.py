# KNN Algorithm using Iris CSV Dataset

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
data = pd.read_csv("Iris.csv")

# Input and Output
X = data.iloc[:, 1:-1].values
y = data.iloc[:, -1].values

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1)

# Create Model
model = KNeighborsClassifier(n_neighbors=3)

# Train Model
model.fit(X_train, y_train)

# Prediction
pred = model.predict(X_test)

# Accuracy
print("Accuracy :", accuracy_score(y_test, pred))

print("\nPredictions:\n")

# Print Correct and Wrong Predictions
for i in range(len(y_test)):

    print("Actual :", y_test[i],
          " Predicted :", pred[i], end=' ')

    if y_test[i] == pred[i]:
        print("-> Correct")

    else:
        print("-> Wrong")