import serial
import csv

# Configure Serial Port
serial_port = 'COM3'  # Update with your port (e.g., /dev/ttyUSB0 on Linux)
baud_rate = 9600

def collect_data(output_file="alzheimers_data.csv"):
    ser = serial.Serial(serial_port, baud_rate, timeout=1)

    # Open file to save data
    with open(output_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["eeg_signal", "heart_rate", "skin_temp", "gsr"])  # Header
        
        try:
            print("Collecting data... Press Ctrl+C to stop.")
            while True:
                line = ser.readline().decode("utf-8").strip()
                if line:
                    data = line.split(",")
                    writer.writerow(data)
                    print(data)
        except KeyboardInterrupt:
            print("Data collection stopped.")
        finally:
            ser.close()

if __name__ == "__main__":
    collect_data()
