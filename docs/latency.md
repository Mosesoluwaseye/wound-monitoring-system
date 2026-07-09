# System Latency Concept

## Overview

The Wound Monitoring System is designed to reduce delay between sensor measurement, processing, prediction, storage, and visualization.

The system pipeline:

Sensor Data Collection
→ Signal Pre-processing
→ Machine Learning Classification
→ Database Storage
→ REST API Transfer
→ Dashboard Visualization


## Sensor Data Latency

The system uses simulated IoT wound monitoring sensors.

Sensor modalities:

- Temperature sensor
- Moisture sensor

Sensor values are collected periodically and transferred as JSON data.

Latency reduction:

- Lightweight JSON format
- Small sensor payload size
- Direct API communication


## Signal Pre-processing Latency

Sensor preprocessing is implemented in:

sensor/preprocessing.py

Processing includes:

- Cleaning sensor readings
- Formatting temperature values
- Formatting moisture values
- Preparing input for machine learning prediction

Latency reduction:

- Minimal processing steps
- Numeric sensor features only
- Real-time preprocessing before classification


## Machine Learning Prediction Latency

Machine learning implementation:

ml/train_model.py
ml/predict.py

The trained classification model predicts wound conditions:

- Stable
- Warning
- Critical

Latency reduction:

- Model is loaded once during backend startup
- Only prediction is executed during requests
- Lightweight classification model


## Database Latency

Database:

SQLite

Sensor measurements and ML predictions are stored after processing.

Latency reduction:

- Optimized database transactions
- Small structured records
- Fast read/write operations


## Backend API Latency

Flask API endpoints provide asynchronous communication support.

Main endpoints:

/sensor-data
/fhir-data

Latency reduction:

- JSON API communication
- Efficient database queries
- Separated processing components


## Complete Data Flow

1. Sensor captures wound measurement
2. Data preprocessing prepares the signal
3. Machine learning model classifies wound status
4. Result is stored in database
5. Dashboard retrieves updated information through API


## Goal

The latency strategy ensures fast sensor processing, real-time wound classification, and efficient healthcare monitoring visualization.
