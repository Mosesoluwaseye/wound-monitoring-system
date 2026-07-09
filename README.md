# Wound Monitoring System


## Run in GitHub Codespaces

Repository:

https://github.com/Mosesoluwaseye/wound-monitoring-system


Open this repository using GitHub Codespaces.

Launch the Wound Monitoring System with one command:

```bash
docker compose up --build
```

Docker will automatically:

- Build the application environment
- Install all required dependencies
- Start the Flask backend server
- Launch the Wound Monitoring System


After the server starts:

1. Open the PORTS tab in GitHub Codespaces.
2. Select port 5000.
3. Set visibility to Public if required.
4. Open the forwarded GitHub Codespaces URL.


Live Codespaces Application:

```text
https://didactic-carnival-jjj5g755px5vfj596-5000.app.github.dev/
```



# Project Description

The Wound Monitoring System is an IoT-based healthcare sensor monitoring application.

The system collects wound sensor measurements, processes sensor signals, predicts wound conditions using machine learning, stores results in a database, and visualizes healthcare information through an interactive dashboard.


System pipeline:

```text
Sensor Measurement

↓

Signal Pre-processing

↓

Machine Learning Classification

↓

SQLite Database Storage

↓

Asynchronous REST API

↓

Dashboard Visualization
```



# Sensor Data System


## Sensor Modality

The system uses simulated IoT wound monitoring hardware.

Implementation:

```text
sensor/sensor_simulator.py
```


Measured sensor signals:

- Temperature sensor readings
- Moisture sensor readings


The sensor module represents a wound monitoring device collecting physiological measurements and transmitting data to the backend API.



## Sensor Signal Pre-processing

Implementation:

```text
sensor/preprocessing.py
```


Processing steps:

- Sensor value validation
- Temperature normalization
- Moisture normalization
- Feature preparation for machine learning classification



## Machine Learning Classification

Implementation:

```text
ml/train_model.py

ml/predict.py
```


Machine learning model:

- Decision Tree Classifier


Input features:

- Temperature
- Moisture level


Prediction output:

- Stable
- Warning
- Critical


Trained model:

```text
ml/wound_classifier.pkl
```



## Database Integration

Database technology:

```text
SQLite + Flask SQLAlchemy
```


Database file:

```text
backend/instance/wound_monitor.db
```


The backend stores:

- Patient information
- Sensor readings
- Machine learning prediction
- Timestamp


The API writes and retrieves sensor data from the database.



## Asynchronous API Access

The backend supports asynchronous communication.

Async endpoints:

```text
GET /sensor-data

POST /sensor-data

GET /fhir-data
```


This supports communication between sensor devices, backend processing, and dashboard visualization.



## Latency Management

Documentation:

```text
docs/latency.md
```


The latency concept includes:

- Sensor transmission latency
- Pre-processing latency
- Machine learning prediction latency
- Database read/write latency
- API response latency



# Features

- Patient registration system
- Wound monitoring dashboard
- Temperature monitoring
- Moisture monitoring
- Sensor simulation
- Sensor signal preprocessing
- Machine learning wound classification
- Database storage
- Async REST API communication
- Healthcare FHIR JSON format support
- Chart.js visualization
- D3.js visualization
- Automated backend testing
- Docker container support
- GitHub Codespaces deployment



# Technologies Used


## Backend

- Python
- Flask
- Flask SQLAlchemy
- SQLite
- Scikit-learn
- REST API
- FHIR JSON


## Frontend

- HTML
- CSS
- JavaScript
- Chart.js
- D3.js


## Testing and Deployment

- Pytest
- Docker
- Docker Compose
- Git
- GitHub Codespaces
- VS Code



# Project Screenshots


## Wound Monitoring Dashboard

![Wound Monitoring Dashboard](dashboard-preview.png)


## Chart.js and D3.js Visualization

![Data Visualization](visualization-preview.png)



# API Endpoints


## Dashboard

```text
GET /
```


## Sensor Data API

```text
GET /sensor-data

POST /sensor-data
```


## Healthcare FHIR Data

```text
GET /fhir-data
```


## Patient Registration

```text
GET /register

POST /register
```


## Delete Patient Record

```text
DELETE /delete/<id>
```



# Local Installation


Clone repository:

```bash
git clone https://github.com/Mosesoluwaseye/wound-monitoring-system.git
```


Open project:

```bash
cd wound-monitoring-system
```


Start:

```bash
docker compose up --build
```


Open:

```text
http://localhost:5000
```



# Automated Testing

Run:

```bash
pytest -v
```


Expected:

```text
3 passed
```



# Project Structure

```text
wound-monitoring-system

├── backend
│   ├── app.py
│   ├── database.py
│   ├── models.py

├── sensor
│   ├── sensor_simulator.py
│   └── preprocessing.py

├── ml
│   ├── train_model.py
│   ├── predict.py
│   └── wound_classifier.pkl

├── database
│   └── schema.sql

├── docs
│   └── latency.md

├── frontend

├── tests

├── Dockerfile

├── docker-compose.yml

├── dashboard-preview.png

├── visualization-preview.png

└── README.md
```



# Development Checklist Completed

- Sensor data simulation
- Sensor signal preprocessing
- Machine learning classification
- ML prediction integration
- SQLite database connection
- Database read/write functionality
- Async API implementation
- Latency management concept
- Flask backend
- Dashboard frontend
- FHIR JSON response
- Chart.js visualization
- D3.js visualization
- Docker containerization
- Automated testing
- GitHub Codespaces support



# Future Improvements

- Connect real ESP32 temperature sensors
- Connect real moisture detection sensors
- Expand ML training dataset
- Add authentication system
- Deploy with cloud database
- Add mobile monitoring application



# Project Purpose

This project demonstrates a sensor-based digital healthcare monitoring system.

It implements the complete workflow from sensor measurement collection, signal processing, machine learning classification, database management, and real-time visualization.