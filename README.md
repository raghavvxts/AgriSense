# AgriSense+

© 2026 Raghav Vats. All rights reserved.

## Overview

This project implements a **Zigbee-based wireless mesh network** using ESP32-H2 devices to collect and transmit RS-485 data to a central system. The network is designed for scalability, reliability, and long-range communication by leveraging Zigbee mesh topology.

The system reads data from an RS-485 module using a MAX485 transceiver connected to ESP32-H2 end devices. These devices transmit the data through a Zigbee mesh network to a coordinator node, which then forwards the data to a Raspberry Pi 4 for visualization on a dashboard.

---

## System Architecture

```
RS-485 Device → MAX485 → ESP32-H2 (End Device / Router)
            ↓
        Zigbee Mesh Network
            ↓
     ESP32-H2 Coordinator
            ↓
        Serial (UART)
            ↓
      Raspberry Pi 4
            ↓
      Dashboard Display
```

---

## Features

* Zigbee-based wireless communication
* Full mesh network support
* ESP32-H2 devices can act as:

  * End devices
  * Routers (for extended coverage)
* RS-485 data acquisition using MAX485
* Reliable long-distance communication via mesh routing
* Centralized data collection using a coordinator node
* Real-time data visualization on Raspberry Pi dashboard

---

## Hardware Requirements

### End Devices / Routers

* ESP32-H2
* MAX485 RS-485 Transceiver Module
* RS-485 compatible sensors/devices

### Coordinator

* ESP32-H2 (configured as Zigbee Coordinator)

### Backend / Visualization

* Raspberry Pi 4
* Serial (UART) connection to coordinator

---

## Network Topology

This project supports a **full Zigbee mesh topology**:

* End devices can also act as routers
* Dedicated ESP32-H2 routers can be added to:

  * Improve signal strength
  * Extend network coverage
  * Increase reliability in large deployments

---

## Data Flow

1. RS-485 device sends data
2. MAX485 converts RS-485 signal to UART
3. ESP32-H2 reads the data
4. Data is transmitted over Zigbee mesh network
5. Coordinator receives aggregated data
6. Coordinator sends data via serial (UART)
7. Raspberry Pi processes and displays data on dashboard

---

## Software Components

### ESP32-H2 Firmware

* Zigbee stack implementation
* UART communication with MAX485
* Routing and mesh networking logic

### Raspberry Pi

* Serial data receiver script
* Data parser and formatter
* Dashboard (custom or web-based UI)

---

## Setup Instructions

### 1. Hardware Setup

* Connect MAX485 to ESP32-H2 UART pins
* Connect RS-485 lines (A/B) to the external device
* Configure DE/RE pins for transmission control

### 2. Firmware Upload

* Flash ESP32-H2 devices with appropriate roles:

  * End Device / Router firmware
  * Coordinator firmware

### 3. Zigbee Network Configuration

* Initialize coordinator
* Join end devices and routers to the network
* Verify mesh connectivity

### 4. Raspberry Pi Setup

* Connect coordinator via UART
* Run serial listener script
* Launch dashboard interface

---

## Use Cases

* Industrial monitoring systems
* Smart agriculture
* Energy monitoring
* Remote sensor networks

---

## Future Improvements

* OTA firmware updates for ESP32-H2
* Enhanced security (Zigbee encryption)
* Cloud integration (MQTT / HTTP APIs)
* Mobile app dashboard


---


## ✨ Key Features

* **🤖 AI Expert Diagnostics:** Upload a soil image to a Deep Learning CNN to detect soil type. The system automatically fetches live hardware sensor data to recommend the optimal crop (via Random Forest) and provides intelligent, rule-based NPK fertilizer and irrigation advice based on live weather forecasts.
* **📈 Interactive Analytics:** Visualize historical soil data (Temperature, Moisture, pH, EC, NPK) on dynamic, multi-line graphs using Chart.js. Includes multi-select filtering for specific sensors and date ranges.
* **🖨️ PDF Lab Reports:** Generate standardized, printable "AgriSense+" diagnostic reports containing farmer details, live sensor readings, and optimal agricultural ranges.
* **📥 CSV Data Export:** Filter and download raw historical sensor data for external spreadsheet analysis.
* **⚙️ Secure Admin Dashboard:** A password-protected settings panel allowing administrators to securely wipe raw database logs and reset database auto-increments.
* **🔄 Automated Background Aggregation:** A silent background worker (`soil_aggregator.py`) that wakes up every 10 seconds to average raw high-frequency Node-RED data into a clean, optimized database for the web dashboard.

---

## 🛠️ Tech Stack

* **Hardware:** Raspberry Pi, NPK/Soil Health Sensors.
* **Data Ingestion:** Node-RED (Writing to SQLite).
* **Backend:** Python 3, Flask, SQLite3.
* **Machine Learning:** TensorFlow/Keras, Scikit-Learn, Pandas, NumPy.
* **Frontend:** HTML5, CSS3, Vanilla JavaScript, Chart.js.
* **Utilities:** fpdf2 (PDF Generation), Werkzeug (Security/File Routing).

---

## 📂 Directory Structure

```text
/home/pi/Desktop/flask/
│
├── main.py                 # Main Flask application & Blueprint registry
├── soil_aggregator.py      # Background worker for averaging DB readings
│
├── weather.py              # Blueprint: Weather & Forecasting
├── expert.py               # Blueprint: AI Diagnostics & ML Models
├── analytics.py            # Blueprint: Chart.js Data Visualization
├── report.py               # Blueprint: PDF Report Generator
├── download.py             # Blueprint: CSV Data Exporter
├── settings.py             # Blueprint: Secure Admin Panel
│
├── TrainedModelWeights.h5  # Keras CNN Weights for Soil Detection
├── CropData.csv            # Training dataset for Crop Prediction
│
├── farmweather.db          # Main Dashboard Database (Aggregated Data)
├── /home/pi/soil_data.db   # Raw Node-RED Database (External)
│
└── templates/              # HTML Frontend Views
    ├── home.html
    ├── expert.html
    ├── analytics.html
    ├── report.html
    ├── download.html
    └── settings.html
```

---

## 🚀 Installation & Setup

### 1. Prerequisites

Ensure your Raspberry Pi has Node-RED running and actively logging sensor data into `/home/pi/soil_data.db` under the table `soil_readings`.

### 2. Set Up the Virtual Environment

Navigate to your project folder and ensure your virtual environment is active:

```bash
cd /home/pi/Desktop/flask
source /home/pi/pi-venv/bin/activate
```

### 3. Install Dependencies

Install the required Python libraries for the web server, machine learning models, and PDF generation:

```bash
pip install flask pandas scikit-learn tensorflow pillow werkzeug fpdf2
```

### 4. Machine Learning Files

Ensure your AI model files (`TrainedModelWeights.h5` and `CropData.csv`) are placed directly in the root of the project folder next to `main.py`.

---

## 💻 Running the Application

To start the dashboard, you must run it using `sudo` (if binding to port 80) and specify the virtual environment's Python path so it can access TensorFlow and Pandas:

```bash
sudo /home/pi/pi-venv/bin/python main.py
```

**What happens on startup?**

- The script will automatically spawn `soil_aggregator.py` in the background.
- The Flask server will boot up.
- Going to the root IP (`http://<your-pi-ip>/`)
- Access the main dashboard hub by navigating to your defined sub-routes (e.g., `/expert`, `/analytics`).

---

## 🔐 Security Note

The `/settings` page contains a "Danger Zone" that allows for the complete deletion of raw sensor logs.

To change this password, generate a new Werkzeug hash in Python and update the `ADMIN_PASSWORD_HASH` variable inside `settings.py`.

---

## 🧠 How the AI Works (Expert Diagnostics)

1. **Soil Analysis:** The uploaded image is resized to `256x256` and fed into a custom CNN architecture to classify the soil into one of 5 categories (Clay, Loam, Sandy, etc.).
2. **Data Sync:** The backend pulls the absolute latest average temperature, moisture, pH, EC, and NPK values from `farmweather.db`.
3. **Crop Prediction:** The sensor parameters are scaled and fed into a Random Forest Classifier trained on `CropData.csv` to predict the most viable crop.
4. **Actionable Insights:** Instead of generic ML outputs, the system generates intelligent, rule-based NPK fertilizer and irrigation recommendations based on live weather forecasts and detected soil conditions.
