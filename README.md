# Wound Monitoring System

![Python](https://img.shields.io/badge/Python-Backend-blue)
![Flask](https://img.shields.io/badge/Flask-API-black)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-green)
![IoT](https://img.shields.io/badge/IoT-Healthcare-orange)

Real-time IoT wound monitoring and healthcare visualization system using sensors, backend APIs, and live dashboards.

---

## Project Overview

This project focuses on improving chronic wound monitoring through digital healthcare technologies and IoT-based sensor systems.

The system is designed to:

- monitor wound conditions in real time
- visualize sensor data
- support healthcare professionals remotely
- improve patient monitoring efficiency

---

## Features

- Real-time sensor monitoring
- Wound image documentation
- Interactive dashboard
- Progress tracking
- Backend APIs
- Healthcare visualization
- Secure authentication
- Data analytics
- Real-time communication
- Sensor simulation support

---

## Technologies

### Hardware

- ESP32
- Temperature Sensors
- Moisture Sensors

### Backend

- Flask
- FastAPI
- MongoDB
- MQTT
- Flask-SocketIO
- JWT Authentication

### Frontend

- React
- Chart.js
- HTML/CSS
- JavaScript

---

## Backend Service

This backend handles:

- sensor data collection
- API communication
- authentication
- MongoDB storage
- MQTT messaging
- real-time sensor updates

---

## API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Backend status |
| `/api/data` | GET | Retrieve sensor readings |
| `/api/data` | POST | Send new sensor readings |
| `/patients` | GET | Retrieve patient information |
| `/analytics` | GET | Retrieve healthcare analytics |

---

## Example Sensor Data

```json
{
  "patient_id": "P001",
  "temperature": 37.5,
  "moisture": 62,
  "status": "stable"
}
```

---

## System Architecture

Sensors  
↓  
ESP32 Microcontroller  
↓  
Flask Backend API  
↓  
MongoDB Database  
↓  
React Dashboard  
↓  
Real-Time Healthcare Visualization

---

## Project Workflow

1. Sensors collect wound data
2. ESP32 sends sensor readings
3. Backend API processes incoming data
4. MongoDB stores patient readings
5. Dashboard visualizes healthcare data
6. Healthcare staff monitor wound conditions remotely

---

## Expert Monitoring System

The platform supports remote healthcare supervision through expert-assisted wound monitoring.

Healthcare professionals can:

- review wound sensor readings remotely
- monitor patient healing progress
- analyze wound temperature and moisture levels
- receive abnormal condition alerts
- document wound progression using images
- track patient recovery over time

The system is designed to improve communication between patients and healthcare professionals through digital healthcare technologies and real-time monitoring systems.

---

## Healthcare Visualization

The dashboard provides:

- real-time wound status visualization
- patient monitoring analytics
- wound healing progression charts
- sensor data history
- healthcare alerts and notifications
- remote monitoring support

---

## Remote Monitoring Workflow

1. Patient sensors collect wound data
2. ESP32 sends data to backend API
3. Backend processes sensor readings
4. MongoDB stores monitoring history
5. Dashboard visualizes wound progression
6. Healthcare experts review patient status remotely
7. Alerts are generated for abnormal readings

---

## Repository Structure

```bash
docs/
backend/
frontend/
hardware/
database/
sensor-data/
diagrams/
assets/
```

---

## Setup Guide

### Install Dependencies

```bash
pip3 install flask flask-socketio flask-cors
```

### Run Backend Server

```bash
python3 backend/app.py
```

### Open Local Server

```text
http://127.0.0.1:5000
```

---

## Screenshots

### Backend API Running

<img width="700" alt="Backend API" src="assets/backend-running.png">

### Dashboard Preview

<img width="700" alt="Dashboard Preview" src="assets/dashboard-preview.png">

---

## Future Improvements

- AI-based wound prediction
- Secure messaging
- Real-time video consultation
- Mobile application support
- Wearable sensor integration
- Cloud deployment
- MQTT live device communication
- Advanced healthcare analytics
- Doctor notification alerts

---

## Research & Academic Focus

This project combines concepts from:

- Internet of Things (IoT)
- Digital Healthcare
- Real-Time Data Visualization
- Remote Patient Monitoring
- Embedded Systems
- Backend API Development
- Healthcare Analytics

---

## Authors

- Oluwaseye Moses

---

## License

This project is licensed under the MIT License.
