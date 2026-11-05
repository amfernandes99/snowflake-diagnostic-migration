-- Check that the replacement dataset contains no unexpected diagnostic records.
SELECT
    VEHICLE_ID,
    DID_ID,
    DID_VALUE,
    RECORDED_AT
FROM {{ ref('replacement_diagnostics') }}

MINUS

SELECT
    VEHICLE_ID,
    DID_ID,
    DID_VALUE,
    RECORDED_AT
FROM AUTOMOTIVE_DB.RAW.LEGACY_DIAGNOSTICS
