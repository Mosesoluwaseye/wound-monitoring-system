import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../backend")))

from app import app


def test_home_page():
    tester = app.test_client()
    response = tester.get("/")
    assert response.status_code == 200


def test_sensor_data_api():
    tester = app.test_client()
    response = tester.get("/sensor-data")
    assert response.status_code == 200


def test_fhir_data_api():
    tester = app.test_client()
    response = tester.get("/fhir-data")
    assert response.status_code == 200