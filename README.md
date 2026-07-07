# Wound Monitoring System


## Run in GitHub Codespaces

Open this repository using GitHub Codespaces.

Install dependencies and launch the Wound Monitoring System:

```bash
cd backend && pip install -r requirements.txt && python app.py
```

After the server starts:

1. Open the PORTS tab in GitHub Codespaces.
2. Select port 5000.
3. Open the forwarded GitHub Codespaces URL.

Example:

```text
https://your-codespace-name-5000.app.github.dev/
```

The Wound Monitoring Dashboard will open in the browser.


## Project Description

The Wound Monitoring System is an interactive healthcare monitoring application designed to visualize wound sensor data.

The system collects patient wound information including:

- Temperature readings
- Moisture levels
- Wound location
- Healing status

Healthcare providers can register patients, monitor wound conditions, search patient records, remove outdated records, and analyze sensor data through an interactive dashboard.

The application supports healthcare data exchange concepts using FHIR-style JSON formatting for wound sensor observations.



## Features

- Patient registration system
- Wound monitoring dashboard
- Temperature tracking
- Moisture monitoring
- Patient search functionality
- Delete patient records
- Automatic dashboard updates
- Healthcare FHIR JSON data format support
- Chart.js temperature history visualization
- Interactive D3.js sensor visualization
- REST API communication
- Automated backend testing
- GitHub Codespaces support


### Wound Status Classification

- Stable
- Warning
- Critical



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

- Git
- GitHub
- GitHub Codespaces
- VS Code



## System Architecture


```text
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
```



## Database Information

Stored patient data:

- Patient ID
- Patient Name
- Age
- Wound Location
- Temperature
- Moisture Level
- Wound Status
- Date and Time Created



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

![Backend](backend-running.png)



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


Open project:

```bash
cd wound-monitoring-system
```


Install requirements and start application:

```bash
cd backend && pip install -r requirements.txt && python app.py
```


Open:

```text
http://127.0.0.1:5000
```


### GitHub Codespaces

When running inside GitHub Codespaces:

1. Open PORTS.
2. Select port 5000.
3. Open the forwarded URL.

Example:

```text
https://your-codespace-name-5000.app.github.dev
```


## Testing


This project includes automated backend tests using Pytest.


Run tests:

```bash
pytest
```


Current tests:

- Home dashboard route test
- Sensor data API test
- FHIR healthcare API test


Successful result:

```text
3 passed
```



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


├── README.md

└── LICENSE
```



## Development Checklist Completed

- Working Flask application
- Database integration
- REST API implementation
- FHIR-style healthcare JSON response
- Frontend dashboard
- Sensor data visualization
- Chart.js implementation
- D3.js implementation
- Automated tests
- Git version control
- GitHub repository
- GitHub Codespaces execution
- Project documentation



## Future Improvements

- Connect physical IoT temperature sensors
- Connect moisture detection sensors
- Add user authentication system
- Add cloud database storage
- Deploy application online
- Add mobile application support
- Add advanced wound healing predictions
- Add healthcare system integration



## Project Purpose

This project demonstrates how digital health technologies can support wound monitoring using sensor data collection, database management, healthcare data formatting, and real-time visualization.

The system shows how healthcare providers can track wound conditions, analyze sensor measurements, and identify possible complications through digital monitoring.