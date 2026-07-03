# Wound Monitoring System


## Project Description

The Wound Monitoring System is an interactive healthcare monitoring application designed to visualize wound sensor data.

The system collects patient wound information such as temperature, moisture level, wound location, and healing status.

Healthcare providers can register patients, monitor wound conditions, search patient records, remove outdated records, and view sensor data through an interactive dashboard.


## Features

- Patient registration system
- Real-time wound monitoring dashboard
- Temperature tracking
- Moisture monitoring
- Patient search functionality
- Delete patient records
- Automatic dashboard updates
- Interactive data visualization
- Status classification:
  - Stable
  - Warning
  - Critical
- Temperature history chart


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

REST API Communication

↓

Frontend Dashboard

↓

Real-Time Data Visualization



## Database Information

The database stores:

- Patient ID
- Patient Name
- Patient Age
- Wound Location
- Temperature Reading
- Moisture Level
- Wound Status
- Date and Time Created



## API Endpoints


### Home Dashboard

GET

/


### View Sensor Data

GET

/sensor-data


### Add Sensor Reading

POST

/sensor-data


### Register Patient

GET / POST

/register


### Delete Patient Record

DELETE

/delete/<id>



## Project Screenshots


### Wound Monitoring Dashboard

![Dashboard](docs/images/dashboard.png)


### Patient Search and Records

![Patient Search](docs/images/search.png)


### Temperature Visualization

![Temperature Chart](docs/images/chart.png)



## How To Run The Project


Clone the repository:

git clone https://github.com/Mosesoluwaseye/wound-monitoring-system.git


Move into the project folder:

cd wound-monitoring-system


Move into backend folder:

cd backend


Install dependencies:

pip install -r requirements.txt


Start Flask server:

python3 app.py


Open the application:

http://127.0.0.1:5000



## Project Structure


wound-monitoring-system

│

├── backend

│   ├── app.py

│   ├── database.py

│   ├── models.py

│   ├── static

│   │   ├── style.css

│   │   └── script.js

│   └── templates

│       ├── index.html

│       └── register.html

│

├── diagrams

│   └── system-architecture.md

│

├── docs

│   └── images

│

└── README.md



## Future Improvements

- Connect physical IoT temperature sensors
- Connect moisture detection sensors
- Add user authentication system
- Add cloud database storage
- Deploy the application online
- Add mobile application support
- Add advanced wound healing predictions


## Project Purpose

This project demonstrates how digital health technologies can support wound monitoring using sensor data collection, database management, and real-time healthcare visualization.

The system shows how healthcare providers can track wound conditions and identify possible complications through digital monitoring.