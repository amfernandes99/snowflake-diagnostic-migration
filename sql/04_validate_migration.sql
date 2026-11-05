# Comparing the legacy and replacement diagnostics tables. Results should be empty if the migration was successful.
SELECT
    VEHICLE_ID,
    DID_ID,
    DID_VALUE,
    RECORDED_AT
FROM AUTOMOTIVE_DB.RAW.LEGACY_DIAGNOSTICS

MINUS

SELECT
    ASSET_REF,
    DIAGNOSTIC_CODE,
    MEASUREMENT,
    EVENT_TIMESTAMP
FROM AUTOMOTIVE_DB.RAW.REPLACEMENT_DIAGNOSTICS;

# Other way around to ensure that the migration was successful. Results should be empty if the migration was successful.
SELECT
    ASSET_REF,
    DIAGNOSTIC_CODE,
    MEASUREMENT,
    EVENT_TIMESTAMP
FROM AUTOMOTIVE_DB.RAW.REPLACEMENT_DIAGNOSTICS

MINUS

SELECT
    VEHICLE_ID,
    DID_ID,
    DID_VALUE,
    RECORDED_AT
FROM AUTOMOTIVE_DB.RAW.LEGACY_DIAGNOSTICS;
