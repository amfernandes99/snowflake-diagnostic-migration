-- Presents the replacement diagnostic data with the legacy column names.

SELECT
    ASSET_REF AS VEHICLE_ID,
    DIAGNOSTIC_CODE AS DID_ID,
    MEASUREMENT AS DID_VALUE,
    EVENT_TIMESTAMP AS RECORDED_AT
FROM {{ source('raw', 'REPLACEMENT_DIAGNOSTICS') }}

