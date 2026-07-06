from flask import Flask, render_template, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///wound_monitoring.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    wound_location = db.Column(db.String(100))
    temperature = db.Column(db.Float)
    moisture = db.Column(db.Float)
    status = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    patients = Patient.query.all()
    return render_template("index.html", patients=patients)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        patient = Patient(
            patient_name=request.form["patient_name"],
            age=request.form["age"],
            wound_location=request.form["wound_location"],
            temperature=request.form["temperature"],
            moisture=request.form["moisture"],
            status=request.form["status"],
        )

        db.session.add(patient)
        db.session.commit()

        return redirect("/")

    return render_template("register.html")


@app.route("/sensor-data", methods=["GET"])
def sensor_data():
    patients = Patient.query.all()

    data = []

    for patient in patients:
        data.append(
            {
                "id": patient.id,
                "patient_name": patient.patient_name,
                "age": patient.age,
                "wound_location": patient.wound_location,
                "temperature": patient.temperature,
                "moisture": patient.moisture,
                "status": patient.status,
            }
        )

    return jsonify(data)


@app.route("/fhir-data")
def fhir_data():
    return jsonify(
        {
            "resourceType": "Observation",
            "status": "final",
            "category": "wound-monitoring",
        }
    )


@app.route("/delete/<int:id>", methods=["DELETE"])
def delete_patient(id):
    patient = Patient.query.get(id)

    if patient:
        db.session.delete(patient)
        db.session.commit()

    return jsonify({"message": "deleted"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)