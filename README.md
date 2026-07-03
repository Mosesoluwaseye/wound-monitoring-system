# Wound Monitoring System

## Project Description

The Wound Monitoring System is an interactive healthcare monitoring application designed to visualize wound sensor data.

The system collects patient wound information such as temperature, moisture level, wound location, and healing status.

Healthcare providers can register patients, monitor wound conditions, search patient records, and view sensor data through a dashboard.


## Features

- Patient registration system
- Real-time wound monitoring dashboard
- Temperature tracking
- Moisture monitoring
- Patient search functionality
- Delete patient records
- Status classification:
  - Stable
  - Warning
  - Critical
- Interactive temperature chart visualization


## Technologies Used

### Backend
- Python
- Flask
- Flask SQLAlchemy
- SQLite Database
- REST API

### Frontend
- HTML
- CSS
- JavaScript
- Chart.js


## System Architecture

Sensor Data Collection

↓

Flask Backend API

↓

SQLite Database

↓

Frontend Dashboard

↓

Real-Time Data Visualization


## Database Information

The database stores:

- Patient ID
- Patient Name
- Age
- Wound Location
- Temperature Reading
- Moisture Level
- Wound Status
- Date and Time


## API Endpoints

### View Sensor Data

GET

/sensor-data


### Add Sensor Reading

POST

/sensor-data


### Register Patient

/register


### Delete Record

/delete/<id>


## How To Run The Project

Clone the repository:

git clone https://github.com/Mosesoluwaseye/wound-monitoring-system.git


Move into backend folder:

cd backend


Install dependencies:

pip install -r requirements.txt


Run Flask:

python3 app.py


Open browser:

http://127.0.0.1:5000


## Future Improvements

- Connect physical IoT sensors
- Add user authentication
- Add cloud database storage
- Deploy online
- Add mobile application support


## Project Purpose

This project demonstrates how digital health technologies can support wound monitoring through data collection, analysis, and visualization.
