import os
import snowflake.connector
from dotenv import load_dotenv

# Load credentials from the .env file
load_dotenv()

# Connect to Snowflake
connection = snowflake.connector.connect(
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA"),
    role=os.getenv("SNOWFLAKE_ROLE"),
    enable_server_session_keep_alive_auto_detection=True
)

print("Successfully connected to Snowflake!")

connection.close()
