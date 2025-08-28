# Realtime-PII-Defense
A Python script that scans CSV data for personally identifiable information (PII), redacts it, and flags records containing PII.

# Steps

*Prepare Input File: Keep your CSV file in the same folder as the script. Ensure the Data_json column contains valid JSON.

*Run the Script:
python3 detector_afthab.py iscp_pii_dataset_-_Sheet1.csv

## PII Detector Deployment Plan

# PII Detector Deployment Plan

I think its better to run the PII detector as a **Sidecar container** alongside our main app. In this way, it can watch the data and mask the sensitive info in realtime without touching the app itself, which is nice because we don’t have to mess with teh existing code 

Its pretty easy to set up, scales automatically as the app grows, and the latency stays low, which is good because nobody likes slow apps. Basically, all incoming data goes through the Sidecar, gets cleaned, and then continues on to storage or APIs. You can even log some stats if needed, just for monitoring and all 

I thought about other options like running it at the network level or in the browser, but with these options, we'll have to deal with a lot of extra setup and it might not catch everything all the time. This approach is simple and safe and easy to manage 


