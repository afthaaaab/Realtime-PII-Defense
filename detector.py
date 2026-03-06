import csv, json, re, sys

if len(sys.argv) < 2:
    print("Usage: python3 detector_afthab.py <input_csv_file>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = "redacted_output.csv"

rows_out = []

with open(input_file, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            data = json.loads(row["Data_json"])
        except:
            print(f"Skipping bad JSON: {row['Data_json']}")
            continue
        
        pii = False

        # Standalone PII
        if "phone" in data and re.fullmatch(r"\d{10}", data["phone"]):
            data["phone"] = data["phone"][:2] + "XXXXXX" + data["phone"][-2:]
            pii = True
        if "aadhar" in data and re.fullmatch(r"\d{12}", data["aadhar"]):
            data["aadhar"] = "XXXX XXXX " + data["aadhar"][-4:]
            pii = True
        if "passport" in data and re.fullmatch(r"[A-Za-z]\d{7}", data["passport"]):
            data["passport"] = data["passport"][0] + "XXXXXXX"
            pii = True
        if "upi_id" in data and "@" in data["upi_id"]:
            parts = data["upi_id"].split('@')
            data["upi_id"] = parts[0][:2] + "XXXX" + "@" + parts[1]
            pii = True

        # Combinatorial PII
        combo_fields = ["name","email","address","device_id","ip_address"]
        if sum(1 for f in combo_fields if f in data and data[f]) >= 2:
            for f in combo_fields:
                if f in data and data[f]:
                    data[f] = "REDACTED_PII"
            pii = True

        row["redacted_data_json"] = json.dumps(data)
        row["is_pii"] = str(pii)
        rows_out.append(row)

# Write output CSV
with open(output_file, "w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=rows_out[0].keys())
    writer.writeheader()
    writer.writerows(rows_out)

print(f"Redacted file saved as {output_file}")
