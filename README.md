# Alzheimer's Detection System

This project demonstrates how to detect Alzheimer's risk using multiple sensors (EEG, heart rate, skin temperature, and galvanic skin response) and Python.

## Features
- Real-time data collection using Arduino
- Risk detection using Python and Isolation Forest
- Visualization of detected Alzheimer's risk patterns

## Hardware Requirements
- Arduino-compatible board (e.g., Arduino Nano)
- Sensors:
  - EEG Sensor
  - Heart Rate Monitor
  - Temperature Sensor
  - Galvanic Skin Response (GSR) Sensor
- USB Cable
- PC with Python and VS Code

## Software Requirements
- Arduino IDE
- Python 3.7 or higher
- Libraries: `pandas`, `scikit-learn`, `matplotlib`, `pyserial`

## Setup Instructions

### Arduino Setup
1. Upload the `Alzheimers_Sensor.ino` sketch to the Arduino.
2. Connect the Arduino to your PC.

### Python Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/faheem09/Alzheimers-Detection-System.git
   cd Alzheimers-Detection-System
   ```
2. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # Windows: env\Scripts\activate
   pip install -r requirements.txt
   ```
3. Run the `data_collection.py` script to collect sensor data:
   ```bash
   python Python_Code/data_collection.py
   ```
4. Run the `alzheimers_detection.py` script to detect Alzheimer's risk:
   ```bash
   python Python_Code/alzheimers_detection.py
   ```

## Example Visualization
![Alzheimer's Risk Detection Plot](example_plot.png)

## License
This project is licensed under the MIT License.
