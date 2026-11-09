-- Check that legacy and replacement datasets contain the same number of records.

SELECT
    (SELECT COUNT(*)
     FROM {{ source('raw', 'LEGACY_DIAGNOSTICS') }})
    -
    (SELECT COUNT(*)
     FROM {{ ref('replacement_diagnostics') }})
    AS RECORD_COUNT_DIFFERENCE

WHERE RECORD_COUNT_DIFFERENCE != 0
