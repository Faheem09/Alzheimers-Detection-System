// Example Arduino code for Alzheimer's data collection
#include <Arduino.h>

void setup() {
  Serial.begin(9600);
  while (!Serial);
  Serial.println("Alzheimer's Data Collection Started");
}

void loop() {
  // Simulate sensor readings (replace with real sensors)
  float eeg_signal = random(0, 100) / 100.0;   // Simulated EEG signal
  float heart_rate = random(60, 100);         // Simulated heart rate (BPM)
  float skin_temp = random(30, 35);           // Simulated skin temperature (°C)
  float gsr = random(500, 1000);              // Simulated galvanic skin response

  // Print data in CSV format
  Serial.print(eeg_signal);
  Serial.print(",");
  Serial.print(heart_rate);
  Serial.print(",");
  Serial.print(skin_temp);
  Serial.print(",");
  Serial.println(gsr);

  delay(100);  // Sampling rate: 10 Hz
}
