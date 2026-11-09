# Diagnostic_migration (dbt project)

This is the dbt part of the project. It takes the replacement platform's diagnostic data
and presents it with the legacy column names, then tests that it matches the legacy extract.

I chose to include the use of dbt in this project as it provided me with a great opportunity to develop my own dbt skills and experience.

## Model

`models/replacement_diagnostics.sql` builds a **view** in `AUTOMOTIVE_DB.ANALYTICS`.
It renames the replacement columns to the legacy names:

| Replacement column | Legacy name |
| --- | --- |
| ASSET_REF | VEHICLE_ID |
| DIAGNOSTIC_CODE | DID_ID |
| MEASUREMENT | DID_VALUE |
| EVENT_TIMESTAMP | RECORDED_AT |

I used a view so it always reflects the current replacement data without storing a copy.

## Sources

Declared in `models/_sources.yml` (source `raw`, schema `AUTOMOTIVE_DB.RAW`):

- `REPLACEMENT_DIAGNOSTICS`: the replacement platform extract the model reads from.
- `LEGACY_DIAGNOSTICS`: the legacy extract the tests compare against.

## Tests

There are 7 tests in total. Each one passes when it returns no rows.

**Generic tests** (in `models/_models.yml`):

1. `not_null` on `VEHICLE_ID`
2. `not_null` on `DID_ID`
3. `not_null` on `RECORDED_AT`
4. `dbt_utils.unique_combination_of_columns` on `VEHICLE_ID`, `DID_ID`, `RECORDED_AT`, so no reading is duplicated

**Singular tests** (in `tests/`):

5. `validate_migration`: every legacy record exists in the replacement view
6. `validate_no_extra_records`: the replacement view has no records that aren't in the legacy data
7. `validate_record_count`: both datasets have the same number of records

## Running it

From the repository root, with a Snowflake profile set up (see the main README):

```bash
dbt deps --project-dir diagnostic_migration
dbt build --project-dir diagnostic_migration
```

`dbt deps` installs `dbt_utils`, and `dbt build` creates the view and runs all 7 tests.