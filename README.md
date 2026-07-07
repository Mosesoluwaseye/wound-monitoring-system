# Wound Monitoring System


## Run in GitHub Codespaces

Open this repository using GitHub Codespaces.

Install dependencies and launch the Wound Monitoring System:

```bash
cd backend && pip install -r requirements.txt && python app.py
```

After the server starts, GitHub Codespaces will automatically create a forwarded Port 5000 URL.

Open the Port 5000 forwarded address from the PORTS tab.

Example:

```text
https://your-codespace-name-5000.app.github.dev/
```

The Wound Monitoring Dashboard will open in the browser.


## Project Description

The Wound Monitoring System is an interactive healthcare monitoring application designed to visualize wound sensor data.

The system manages patient wound information including:

- Temperature readings
- Moisture levels
- Wound location
- Healing status

Healthcare providers can register patients, search records, remove patient information, and monitor wound conditions through an interactive dashboard.

The system also demonstrates healthcare interoperability concepts using FHIR-style JSON data formatting.


## Features

- Patient registration system
- Wound monitoring dashboard
- Temperature tracking
- Moisture monitoring
- Patient search functionality
- Delete patient records
- Automatic dashboard updates
- REST API support
- Healthcare FHIR JSON response
- Chart.js temperature visualization
- D3.js sensor data visualization
- Automated backend testing with Pytest


## Technologies Used


### Backend

- Python
- Flask
- Flask SQLAlchemy
- SQLite
- REST API
- FHIR JSON


### Frontend

- HTML
- CSS
- JavaScript
- Chart.js
- D3.js


### Testing

- Pytest


## System Architecture

Sensor Data Collection

↓

Flask Backend API

↓

SQLite Database

↓

FHIR JSON API

↓

Frontend Dashboard

↓

Chart.js and D3.js Visualization



## Database Information

Stored patient data:

- Patient ID
- Patient Name
- Age
- Wound Location
- Temperature
- Moisture Level
- Wound Status
- Creation Time



## API Endpoints


### Dashboard

GET /

Displays the main monitoring dashboard.


### Sensor Data API

GET /sensor-data

Returns wound sensor information in JSON format.


### Healthcare FHIR Data

GET /fhir-data

Returns healthcare observation data using FHIR-style JSON.


### Patient Registration

GET /register

POST /register


### Delete Patient

DELETE /delete/<id>



## Automated Testing

The project includes backend tests.

Run:

```bash
pytest -v
```

Expected result:

```text
3 passed
```



## Project Screenshots


### Wound Monitoring Dashboard

![Dashboard](dashboard-preview.png)


### Backend Running Successfully

![Backend Running](backend-running.png)



## Data Visualization


### Chart.js

Displays wound temperature history using charts.


### D3.js

Creates interactive visualization from live sensor JSON data.



## Local Installation

Clone repository:

```bash
git clone https://github.com/Mosesoluwaseye/wound-monitoring-system.git
```

Move into project:

```bash
cd wound-monitoring-system
```

Start application:

```bash
cd backend && pip install -r requirements.txt && python app.py
```


For local computers open:

```text
http://127.0.0.1:5000
```


For GitHub Codespaces:

Use the forwarded Port 5000 URL.



## Project Structure

```text
wound-monitoring-system

├── backend
│   ├── app.py
│   ├── database.py
│   ├── models.py
│   ├── static
│   └── templates

├── database
├── diagrams
├── docs
├── frontend
├── hardware
├── sensor-data
├── tests
│   └── test_app.py

└── README.md
```



## Future Improvements

- Connect IoT wound sensors
- Add authentication system
- Add cloud database
- Add deployment server
- Add mobile support
- Add wound healing prediction
- Improve healthcare integration



## Project Purpose

This project demonstrates how digital healthcare applications can support wound monitoring using:

- Sensor data processing
- Database management
- REST APIs
- Healthcare data formatting
- Interactive visualization
- Automated software testing
