#include <WiFi.h>
#include <HTTPClient.h>

// WiFi information
const char* ssid = "YOUR_WIFI_NAME";
const char* password = "YOUR_WIFI_PASSWORD";

// Flask backend API endpoint
String serverURL = "http://YOUR_SERVER_IP:5000/sensor-data";


void setup() {

  Serial.begin(115200);

  WiFi.begin(ssid, password);

  Serial.println("Connecting to WiFi");


  while (WiFi.status() != WL_CONNECTED) {

    delay(1000);

    Serial.println(".");

  }


  Serial.println("Connected successfully");
}


void loop() {


  if (WiFi.status() == WL_CONNECTED) {


    HTTPClient http;


    http.begin(serverURL);


    http.addHeader("Content-Type", "application/json");


    float temperature = random(360, 390) / 10.0;

    int moisture = random(40, 90);


    String status;


    if (temperature > 38.0) {

      status = "Infection Risk";

    } else {

      status = "Normal";

    }


    String jsonData = "{";

    jsonData += "\"temperature\":";

    jsonData += temperature;


    jsonData += ",\"moisture\":";

    jsonData += moisture;


    jsonData += ",\"status\":\"";

    jsonData += status;

    jsonData += "\"}";


    http.POST(jsonData);


    Serial.println(jsonData);


    http.end();

  }


  delay(3000);
}