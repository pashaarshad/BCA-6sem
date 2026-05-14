# SVM Classifier using Iris CSV Dataset

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix

# Load Dataset
data = pd.read_csv("Iris.csv")

# Input and Output
X = data.iloc[:, 1:-1].values
y = data.iloc[:, -1].values

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Feature Scaling
# Below 3 lines are optional

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create SVM Model
model = SVC(kernel='linear')

# Train Model
model.fit(X_train, y_train)

# Prediction
pred = model.predict(X_test)

# Accuracy
print("Accuracy :", accuracy_score(y_test, pred))

# Confusion Matrix
print("\nConfusion Matrix:\n")

print(confusion_matrix(y_test, pred))