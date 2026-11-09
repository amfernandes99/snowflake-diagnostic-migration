-- Check that all legacy diagnostic records exist in the replacement dataset.
SELECT
    VEHICLE_ID,
    DID_ID,
    DID_VALUE,
    RECORDED_AT
FROM {{ source('raw', 'LEGACY_DIAGNOSTICS') }}

MINUS

SELECT
    VEHICLE_ID,
    DID_ID,
    DID_VALUE,
    RECORDED_AT
FROM {{ ref('replacement_diagnostics') }}
