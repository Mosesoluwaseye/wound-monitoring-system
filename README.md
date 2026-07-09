# Wound Monitoring System


## Run in GitHub Codespaces

Repository:

https://github.com/Mosesoluwaseye/wound-monitoring-system


Open this repository using GitHub Codespaces.

Launch the Wound Monitoring System:

```bash
docker compose up --build
```

Docker automatically:

- Builds the application environment
- Installs dependencies
- Starts the Flask backend server
- Launches the Wound Monitoring System


After startup:

1. Open the PORTS tab in GitHub Codespaces
2. Select port 5000
3. Set visibility to Public if required
4. Open the forwarded Codespaces URL


Live Application:

```text
https://didactic-carnival-jjj5g755px5vfj596-5000.app.github.dev/
```



# Project Description

The Wound Monitoring System is an IoT-based healthcare sensor monitoring system.

The project implements a complete sensor data pipeline:

```text
IoT Sensor Measurement

↓

Sensor Signal Pre-processing

↓

Machine Learning Classification

↓

Database Storage

↓

Asynchronous REST API Communication

↓

Dashboard Visualization
```


The system collects wound sensor measurements, processes sensor signals, predicts wound conditions using machine learning, stores healthcare records, and visualizes patient data.



# Sensor Hardware Concept


## Sensor Modality

The prototype uses simulated IoT wound monitoring sensors representing physical healthcare hardware.

Implementation:

```text
sensor/sensor_simulator.py
```


Sensor measurements:

- Temperature sensor readings
- Moisture sensor readings


The simulated sensor represents an IoT wound monitoring device similar to hardware sensors connected through microcontrollers such as ESP32.

The sensor module generates wound measurements and transfers them into the backend processing system.



# Sensor Signal Pre-processing

Implementation:

```text
sensor/preprocessing.py
```


Raw sensor data processing includes:

- Sensor data validation
- Removing invalid measurements
- Temperature normalization
- Moisture normalization
- Feature preparation for machine learning


Processed sensor features are sent into the machine learning classification pipeline.



# Machine Learning Classification

Machine learning implementation:

```text
ml/train_model.py

ml/predict.py
```


Algorithm:

```text
Decision Tree Classifier
```


Input features:

- Wound temperature
- Wound moisture level


Prediction classes:

- Stable
- Warning
- Critical


Trained model:

```text
ml/wound_classifier.pkl
```


The machine learning model analyzes sensor measurements and predicts wound condition status automatically.



# Database Integration

Database system:

```text
SQLite + Flask SQLAlchemy
```


Database location:

```text
backend/instance/wound_monitor.db
```


Stored information:

- Patient ID
- Patient information
- Temperature measurements
- Moisture measurements
- ML classification result
- Timestamp


The backend writes sensor results into the database and retrieves stored measurements through API endpoints.



# Asynchronous API Communication

The backend supports asynchronous data access between sensors, database, and dashboard.

Implemented endpoints:

```text
GET /sensor-data

POST /sensor-data

GET /fhir-data
```


The API allows:

- Real-time sensor communication
- Database access
- Healthcare data exchange
- Dashboard updates



# Latency Management Concept

Documentation:

```text
docs/latency.md
```


Measured system flow:

```text
Sensor Capture

↓

Pre-processing

↓

Machine Learning Prediction

↓

Database Operation

↓

API Response

↓

Dashboard Update
```


Latency reduction methods:

- Lightweight JSON sensor messages
- Local ML prediction
- Efficient database queries
- REST API communication



# Features

- Patient registration system
- IoT sensor simulation
- Temperature monitoring
- Moisture monitoring
- Sensor signal preprocessing
- Machine learning wound classification
- Database storage
- Asynchronous REST API
- Healthcare FHIR JSON format
- Interactive dashboard
- Chart.js visualization
- D3.js visualization
- Automated testing
- Docker deployment
- GitHub Codespaces support



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


## Deployment

- Docker
- Docker Compose
- GitHub Codespaces



# Project Screenshots


## Dashboard

![Wound Monitoring Dashboard](dashboard-preview.png)


## Visualization

![Data Visualization](visualization-preview.png)



# API Endpoints


Dashboard:

```text
GET /
```


Sensor Data:

```text
GET /sensor-data

POST /sensor-data
```


FHIR Healthcare Data:

```text
GET /fhir-data
```


Patient Registration:

```text
GET /register

POST /register
```


Delete Record:

```text
DELETE /delete/<id>
```



# Installation


Clone:

```bash
git clone https://github.com/Mosesoluwaseye/wound-monitoring-system.git
```


Enter project:

```bash
cd wound-monitoring-system
```


Run:

```bash
docker compose up --build
```


Open:

```text
http://localhost:5000
```



# Testing

Run:

```bash
pytest -v
```


Expected result:

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

├── README.md

└── LICENSE
```



# Completed Requirements

- Sensor data system
- Sensor preprocessing
- Machine learning prediction
- ML model integration
- Database storage
- Database loading
- Async API routes
- Latency concept
- Docker containerization
- Healthcare JSON formatting
- Dashboard visualization
- Automated tests



# Future Improvements

- Connect physical ESP32 sensors
- Add real temperature hardware
- Add real moisture hardware
- Increase ML training data
- Add authentication
- Deploy cloud database
- Add mobile monitoring



# Project Purpose

This project demonstrates a complete healthcare IoT monitoring workflow.

It connects sensor data acquisition, signal processing, machine learning classification, database management, API communication, and real-time visualization into one digital wound monitoring system.