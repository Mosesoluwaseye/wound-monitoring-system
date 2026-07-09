import pickle

from sklearn.ensemble import RandomForestClassifier


"""
Machine Learning Training Module

Model:
Random Forest Classifier

Input Features:
- Temperature sensor value
- Moisture sensor value

Prediction Classes:
- Stable wound condition
- Warning condition
- Critical condition
"""


training_data = [

    [36.5, 40],
    [36.8, 45],
    [37.2, 55],

    [38.5, 70],
    [38.8, 75],

    [40.0, 90],
    [41.0, 95]

]


labels = [

    "Stable",
    "Stable",
    "Stable",

    "Warning",
    "Warning",

    "Critical",
    "Critical"

]


model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


model.fit(
    training_data,
    labels
)


with open(
    "ml/wound_classifier.pkl",
    "wb"
) as file:

    pickle.dump(
        model,
        file
    )


print(
    "Wound classification model trained successfully"
)