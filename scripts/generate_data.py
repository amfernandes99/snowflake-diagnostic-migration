
import csv
import random
from datetime import datetime, timedelta

random.seed(42)

records = []
start_date = datetime(2026, 1, 1, 9, 0)

# Generate 100 fictional diagnostic records
for i in range(100):
    record = {
        "vehicle_id": f"VEH{i % 20 + 1:03d}",
        "did_id": f"DID_{i % 3 + 1:03d}",
        "did_value": random.randint(10, 100),
        "recorded_at": (start_date + timedelta(hours=i)).isoformat()
    }

    records.append(record)

# Create the legacy data extract
with open("data/legacy_diagnostics.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=records[0].keys())
    writer.writeheader()
    writer.writerows(records)

# Create the replacement data extract
with open("data/replacement_diagnostics.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "asset_ref", "diagnostic_code",
        "measurement", "event_timestamp"
    ])

    for record in records:
        writer.writerow([
            record["vehicle_id"],
            record["did_id"],
            record["did_value"],
            record["recorded_at"]
        ])

print("Both diagnostic datasets generated successfully.")
