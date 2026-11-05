# This script loads CSV files into Snowflake tables.
import os
import snowflake.connector
from dotenv import load_dotenv

load_dotenv()

# Connect to Snowflake
conn = snowflake.connector.connect(
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database="AUTOMOTIVE_DB",
    schema="RAW",
    role=os.getenv("SNOWFLAKE_ROLE"),
    enable_server_session_keep_alive_auto_detection=True
)

# Match CSV files to Snowflake tables
files = {
    "legacy_diagnostics.csv": "LEGACY_DIAGNOSTICS",
    "replacement_diagnostics.csv": "REPLACEMENT_DIAGNOSTICS"
}

cursor = conn.cursor()

try:
    for filename, table in files.items():

        # Get the full file path
        path = os.path.abspath(f"data/{filename}").replace("\\", "/")

        # Upload the file
        cursor.execute(
            f"PUT 'file://{path}' @DIAGNOSTIC_STAGE "
            f"AUTO_COMPRESS=FALSE OVERWRITE=TRUE"
        )

        # Replace the existing records
        cursor.execute(f"TRUNCATE TABLE {table}")

        cursor.execute(f"""
            COPY INTO {table}
            FROM @DIAGNOSTIC_STAGE/{filename}
            FILE_FORMAT = (
                TYPE = CSV
                SKIP_HEADER = 1
                TIMESTAMP_FORMAT = 'AUTO'
            )
            FORCE = TRUE
            ON_ERROR = ABORT_STATEMENT
        """)

        # Check the number of records
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        print(f"{table}: {cursor.fetchone()[0]} records")

finally:
    cursor.close()
    conn.close()
