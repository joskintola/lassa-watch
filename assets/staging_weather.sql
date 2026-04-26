/* @bruin
name: staging.weather
type:  duckdb.sql
materialization:
  type: table

depends:
  - raw.weather

@bruin */

SELECT
    state,
    YEAR(CAST(date AS DATE)) AS year,
    MONTH(CAST(date AS DATE)) AS month,
    AVG(temperature_c) AS avg_temperature_c,
    SUM(precipitation_mm) AS total_precipitation_mm,
    AVG(humidity_percent) AS avg_humidity_percent
FROM raw.weather
GROUP BY state, YEAR(CAST(date AS DATE)), MONTH(CAST(date AS DATE))