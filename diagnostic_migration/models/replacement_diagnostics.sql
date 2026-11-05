-- This validates the migration of the legacy diagnostics table to the replacement diagnostics table --

SELECT
    ASSET_REF AS VEHICLE_ID,
    DIAGNOSTIC_CODE AS DID_ID,
    MEASUREMENT AS DID_VALUE,
    EVENT_TIMESTAMP AS RECORDED_AT
FROM {{ source('raw', 'REPLACEMENT_DIAGNOSTICS') }}

