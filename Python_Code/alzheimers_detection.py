import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

def detect_alzheimers(input_file="alzheimers_data.csv"):
    # Load Alzheimer's Data
    data = pd.read_csv(input_file)
    for col in ["eeg_signal", "heart_rate", "skin_temp", "gsr"]:
        data[col] = pd.to_numeric(data[col], errors="coerce")
    data = data.dropna()

    # Train Unsupervised Model
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(data)

    # Detect Anomalies
    data["alzheimers_risk"] = model.predict(data)
    data["alzheimers_risk"] = data["alzheimers_risk"].apply(lambda x: 1 if x == -1 else 0)

    # Visualize EEG Signals with Detected Anomalies
    plt.figure(figsize=(12, 8))
    plt.plot(data.index, data["eeg_signal"], label="EEG Signal")
    plt.scatter(data.index[data["alzheimers_risk"] == 1], 
                data["eeg_signal"][data["alzheimers_risk"] == 1], color="red", label="Detected Risk")
    plt.legend()
    plt.title("EEG Signal with Detected Alzheimer's Risk")
    plt.show()

if __name__ == "__main__":
    detect_alzheimers()
