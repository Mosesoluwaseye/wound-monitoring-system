import requests
import random
import time
import os


"""
ESP32 Wound Monitoring Sensor Simulation

Sensor Modality:
- Temperature Sensor
- Moisture Detection Sensor

The simulated hardware captures wound measurements
and sends readings to the backend API.
"""


API_URL = os.getenv(
    "SENSOR_API_URL",
    "http://localhost:5000/sensor-data"
)


def collect_sensor_data():

    sensor_data = {

        "patient_id": "P001",

        "patient_name": "Sensor Patient",

        "age": 45,

        "wound_location": "Left Leg",

        "temperature": round(random.uniform(36.0, 41.0), 2),

        "moisture": random.randint(20, 95)

    }

    return sensor_data



while True:

    data = collect_sensor_data()


    try:

        response = requests.post(
            API_URL,
            json=data
        )


        print(
            "Sensor data transmitted:",
            data
        )


    except Exception as error:

        print(
            "Transmission failed:",
            error
        )


    time.sleep(2)