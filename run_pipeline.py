# Automation script to run the entire diagnostic data pipeline
import subprocess
import sys

# Generate synthetic diagnostic data
subprocess.run(
    [sys.executable, "scripts/generate_data.py"],
    check=True
)

# Load the CSV files into Snowflake
subprocess.run(
    [sys.executable, "scripts/load_to_snowflake.py"],
    check=True
)

# Run dbt models and tests
subprocess.run(
    ["dbt", "build", "--project-dir", "diagnostic_migration"],
    check=True
)

print("Pipeline completed successfully!")
