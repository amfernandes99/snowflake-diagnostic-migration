
import os
import pandas as pd
import streamlit as st
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
    schema="ANALYTICS",
    role=os.getenv("SNOWFLAKE_ROLE")
)


# Get legacy diagnostic data
cursor = conn.cursor()
cursor.execute("SELECT * FROM RAW.LEGACY_DIAGNOSTICS")

legacy_data = cursor.fetchall()
legacy_columns = [col[0] for col in cursor.description]

# Get replacement diagnostic data
cursor.execute("SELECT * FROM ANALYTICS.REPLACEMENT_DIAGNOSTICS")

replacement_data = cursor.fetchall()
replacement_columns = [col[0] for col in cursor.description]


cursor.close()
conn.close()

# Display dashboard
st.title("Automotive Diagnostic Migration")

legacy_df = pd.DataFrame(legacy_data, columns=legacy_columns)
replacement_df = pd.DataFrame(replacement_data, columns=replacement_columns)


# Compare legacy and replacement records
comparison = legacy_df.merge(
    replacement_df,
    on=["VEHICLE_ID", "DID_ID", "DID_VALUE", "RECORDED_AT"],
    how="outer",
    indicator=True
)

# Count matching and mismatching records
matching_records = (comparison["_merge"] == "both").sum()
mismatching_records = (comparison["_merge"] != "both").sum()


# Display metrics
col1, col2, col3 = st.columns(3)

col1.metric("Legacy Records", len(legacy_df))
col2.metric("Replacement Records", len(replacement_df))
col3.metric("Matching Records", matching_records)

st.metric("Mismatching Records", mismatching_records)


# Migration validation status
if mismatching_records == 0 and len(legacy_df) == len(replacement_df):
    st.success("Migration Validation: PASSED")
else:
    st.error("Migration Validation: FAILED")




st.subheader("Legacy Diagnostics")
st.dataframe(legacy_df)

st.subheader("Replacement Diagnostics")
st.dataframe(replacement_df)

