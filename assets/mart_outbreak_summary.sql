/* @bruin
name: mart.outbreak_summary
type:  duckdb.sql
materialization:
  type: table

depends:
  - mart.lassa_climate

custom_checks:
  - name: data is not empty
    query: SELECT COUNT(*) FROM mart.outbreak_summary
    value: 8

@bruin */

SELECT
    state,
    MIN(year) AS first_year,
    MAX(year) AS last_year,
    SUM(confirmed_cases) AS total_confirmed,
    SUM(deaths) AS total_deaths,
    ROUND(AVG(cfr_percent), 2) AS avg_cfr_percent,
    MAX(confirmed_cases) AS peak_confirmed_cases,
    MAX(attack_rate_per_100k) AS peak_attack_rate,
    ROUND(AVG(annual_precipitation_mm), 2) AS avg_annual_rainfall_mm,
    ROUND(AVG(avg_annual_temp_c), 2) AS avg_annual_temp_c
FROM mart.lassa_climate
GROUP BY state
ORDER BY total_confirmed DESC