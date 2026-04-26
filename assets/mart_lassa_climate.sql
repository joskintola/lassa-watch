/* @bruin

name: mart.lassa_climate
type:  duckdb.sql

materialization:
  type: table

depends:
  - staging.lassa_cases
  - staging.weather
  - raw.population
  - raw.healthcare

columns:
  - name: year
    type: BIGINT
  - name: state
    type: VARCHAR
  - name: suspected_cases
    type: BIGINT
  - name: confirmed_cases
    type: BIGINT
  - name: deaths
    type: BIGINT
  - name: cfr_percent
    type: DOUBLE
  - name: positivity_rate
    type: DOUBLE
  - name: population
    type: BIGINT
  - name: attack_rate_per_100k
    type: DOUBLE
  - name: hospitals
    type: BIGINT
  - name: lassa_treatment_centres
    type: BIGINT
  - name: health_workers_per_10k
    type: BIGINT
  - name: avg_annual_temp_c
    type: DOUBLE
  - name: annual_precipitation_mm
    type: DOUBLE
  - name: avg_annual_humidity
    type: DOUBLE

@bruin */

SELECT
    l.year,
    l.state,
    l.suspected_cases,
    l.confirmed_cases,
    l.deaths,
    l.cfr_percent,
    l.positivity_rate,
    p.population,
    ROUND(l.confirmed_cases * 100000.0 / p.population, 2) AS attack_rate_per_100k,
    h.hospitals,
    h.lassa_treatment_centres,
    h.health_workers_per_10k,
    AVG(w.avg_temperature_c) AS avg_annual_temp_c,
    SUM(w.total_precipitation_mm) AS annual_precipitation_mm,
    AVG(w.avg_humidity_percent) AS avg_annual_humidity
FROM staging.lassa_cases l
LEFT JOIN raw.population p ON l.state = p.state
LEFT JOIN raw.healthcare h ON l.state = h.state
LEFT JOIN staging.weather w ON l.state = w.state AND l.year = w.year
GROUP BY
    l.year, l.state, l.suspected_cases, l.confirmed_cases,
    l.deaths, l.cfr_percent, l.positivity_rate, p.population,
    h.hospitals, h.lassa_treatment_centres, h.health_workers_per_10k
