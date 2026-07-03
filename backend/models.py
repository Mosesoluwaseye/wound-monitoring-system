from database import db
from datetime import datetime

class SensorData(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    patient_id = db.Column(db.String(20), nullable=False)

    patient_name = db.Column(db.String(100), nullable=False)

    age = db.Column(db.Integer, nullable=False)

    wound_location = db.Column(db.String(100), nullable=False)

    temperature = db.Column(db.Float, nullable=False)

    moisture = db.Column(db.Integer, nullable=False)

    status = db.Column(db.String(20), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "patient_id": self.patient_id,
            "patient_name": self.patient_name,
            "age": self.age,
            "wound_location": self.wound_location,
            "temperature": self.temperature,
            "moisture": self.moisture,
            "status": self.status,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }