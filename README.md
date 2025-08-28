# Realtime-PII-Defense
A Python script that scans CSV data for personally identifiable information (PII), redacts it, and flags records containing PII.

# Steps

*Prepare Input File: Keep your CSV file in the same folder as the script. Ensure the Data_json column contains valid JSON.

*Run the Script:
python3 detector_afthab.py iscp_pii_dataset_-_Sheet1.csv

## PII Detector Deployment Plan

I suggest running the PII detector as a **Sidecar container** alongside our main app. This way, it can check and redact sensitive info in real-time without changing the app

It’s simple and scales automatically with the app and keeps latency low. the incoming data passes through the Sidecar, gets cleaned, and then goess to storage or APIs

This is better than a network level or browser solution because it covers all data and is easy to update independently. Overall it’s safe, efficient, and verry easy to maintain

