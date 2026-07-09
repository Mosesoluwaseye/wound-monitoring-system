from sklearn.tree import DecisionTreeClassifier
import joblib
import os


# Simulated wound sensor training data
# Format: temperature, moisture

X = [
    [36.5, 40],
    [37.0, 45],
    [37.5, 55],
    [38.0, 65],
    [39.0, 75],
    [40.0, 85],
    [35.8, 35],
    [38.7, 70],
    [39.5, 90],
]


# Classification labels

y = [
    "Stable",
    "Stable",
    "Stable",
    "Warning",
    "Warning",
    "Critical",
    "Stable",
    "Warning",
    "Critical",
]


# Train machine learning model

model = DecisionTreeClassifier()

model.fit(X, y)


# Save trained model

model_path = "ml/wound_classifier.pkl"

joblib.dump(model, model_path)


print("Wound classification model trained successfully")
print("Saved:", model_path)