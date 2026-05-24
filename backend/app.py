from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Wound Monitoring Backend Running"
    })

@app.route("/patients")
def patients():
    return jsonify([
        {
            "patient_id": "P001",
            "temperature": 37.2,
            "moisture": 58,
            "status": "stable"
        },
        {
            "patient_id": "P002",
            "temperature": 38.1,
            "moisture": 71,
            "status": "warning"
        }
    ])

@app.route("/analytics")
def analytics():
    return jsonify({
        "active_patients": 2,
        "alerts": 1,
        "system_status": "online"
    })

if __name__ == "__main__":
    app.run(debug=True)
