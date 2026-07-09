import pickle


"""
Machine Learning Prediction Module

Receives processed sensor readings
and predicts wound condition.
"""


with open(
    "ml/wound_classifier.pkl",
    "rb"
) as file:

    model = pickle.load(file)



def classify_wound(
    temperature,
    moisture
):

    prediction = model.predict(
        [
            [
                temperature,
                moisture
            ]
        ]
    )


    return prediction[0]