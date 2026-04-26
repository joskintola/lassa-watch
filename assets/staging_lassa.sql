/* @bruin
name: staging.lassa_cases
type: duckdb.sql
materialization:
  type: table

depends:
  - raw.lassa_cases

columns:
  - name: year
    type: integer
    checks:
      - name: not_null
  - name: state
    type: string
    checks:
      - name: not_null
      - name: accepted_values
        value: ["Ondo", "Edo", "Bauchi", "Taraba", "Ebonyi", "Plateau", "Benue", "Kogi"]
  - name: confirmed_cases
    type: integer
    checks:
      - name: not_null
      - name: positive
  - name: deaths
    type: integer
    checks:
      - name: not_null

@bruin */

SELECT
    year,
    state,
    suspected_cases,
    confirmed_cases,
    deaths,
    cfr_percent,
    state_share_percent,
    ROUND(confirmed_cases * 1.0 / NULLIF(suspected_cases, 0) * 100, 2) AS positivity_rate
FROM raw.lassa_cases
WHERE confirmed_cases > 0