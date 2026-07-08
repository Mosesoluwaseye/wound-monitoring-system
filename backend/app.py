from flask import Flask, jsonify, request, render_template, redirect
from flask_cors import CORS
from database import db
from models import SensorData
import random
import os


app = Flask(__name__)

CORS(app)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///wound_monitor.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)


with app.app_context():
    db.create_all()



@app.route("/")
def home():
    return render_template("index.html")



@app.route("/register")
def register_page():
    return render_template("register.html")



@app.route("/register", methods=["POST"])
def register_patient():

    reading = SensorData(
        patient_id=request.form["patient_id"],
        patient_name=request.form["patient_name"],
        age=int(request.form["age"]),
        wound_location=request.form["wound_location"],
        temperature=float(request.form["temperature"]),
        moisture=int(request.form["moisture"]),
        status=request.form["status"]
    )

    db.session.add(reading)
    db.session.commit()

    return redirect("/")



@app.route("/sensor-data", methods=["GET"])
def get_sensor_data():

    readings = SensorData.query.all()

    return jsonify([reading.to_dict() for reading in readings])



@app.route("/fhir-data", methods=["GET"])
def get_fhir_data():

    readings = SensorData.query.all()

    fhir_data = []

    for reading in readings:

        observation = {

            "resourceType": "Observation",

            "status": "final",

            "category": [
                {
                    "text": "Wound Monitoring"
                }
            ],

            "code": {
                "text": "Wound Sensor Measurement"
            },

            "subject": {

                "reference": "Patient/" + reading.patient_id,

                "display": reading.patient_name
            },

            "component": [

                {
                    "code": {
                        "text": "Temperature"
                    },

                    "valueQuantity": {
                        "value": reading.temperature,
                        "unit": "Celsius"
                    }
                },

                {
                    "code": {
                        "text": "Moisture"
                    },

                    "valueQuantity": {
                        "value": reading.moisture,
                        "unit": "%"
                    }
                }
            ],

            "effectiveDateTime":
            reading.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }

        fhir_data.append(observation)


    return jsonify({

        "resourceType": "Bundle",

        "type": "collection",

        "entry": fhir_data
    })




@app.route("/sensor-data", methods=["POST"])
def add_sensor_data():

    data = request.get_json()

    reading = SensorData(

        patient_id=data["patient_id"],

        patient_name=data["patient_name"],

        age=data["age"],

        wound_location=data["wound_location"],

        temperature=data["temperature"],

        moisture=data["moisture"],

        status=data["status"]
    )

    db.session.add(reading)
    db.session.commit()

    return jsonify({

        "message": "Sensor data saved successfully!"
    })



@app.route("/delete/<int:id>", methods=["DELETE"])
def delete_patient(id):

    reading = SensorData.query.get(id)

    if reading:

        db.session.delete(reading)
        db.session.commit()

        return jsonify({

            "message": "Patient deleted successfully"
        })


    return jsonify({

        "message": "Patient not found"
    })



@app.route("/add-test-data")
def add_test_data():

    names = [
        "John Doe",
        "Mary Smith",
        "Michael Brown",
        "Sarah Johnson",
        "David Wilson"
    ]


    wounds = [
        "Left Foot",
        "Right Foot",
        "Left Leg",
        "Right Leg",
        "Left Arm"
    ]


    temperature = round(random.uniform(36.5, 40.5), 1)

    moisture = random.randint(30, 80)


    if temperature < 37.8:

        status = "stable"

    elif temperature < 39:

        status = "warning"

    else:

        status = "critical"



    reading = SensorData(

        patient_id=f"P{random.randint(100,999)}",

        patient_name=random.choice(names),

        age=random.randint(25,85),

        wound_location=random.choice(wounds),

        temperature=temperature,

        moisture=moisture,

        status=status
    )


    db.session.add(reading)
    db.session.commit()


    return jsonify({

        "message": "Random patient added successfully!",

        "patient": reading.to_dict()
    })



if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=True
    )