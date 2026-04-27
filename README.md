
# LassaWatch 🦠
### Nigeria Lassa Fever Surveillance Pipeline built with Bruin

A data engineering pipeline that ingests, transforms, and analyzes Lassa fever outbreak data across 8 high-burden Nigerian states, enriched with climate and healthcare infrastructure data.

---

## 🎯 Project Overview

Nigeria accounts for the majority of global Lassa fever cases. This pipeline combines epidemiological data from NCDC situation reports with weather data and healthcare capacity metrics to answer critical public health questions:

- Which states carry the highest burden and case fatality rate?
- Does rainfall and humidity correlate with outbreak peaks?
- How does healthcare infrastructure affect survival rates?
- How has the outbreak evolved from 2021 to 2025?

---

## 📊 Data Sources

| Source | Data | Method |
|--------|------|--------|
| NCDC Situation Reports | Lassa cases, deaths, CFR by state (2021–2025) | Python (CSV) |
| Open-Meteo Archive API | Daily temperature, precipitation, humidity | Python (API) |
| NBS Nigeria / WorldPop | State population estimates | Python (static) |
| NCDC / WHO AFRO | Hospital count, LTCs, health workers per 10k | Python (static) |

**States covered:** Ondo, Edo, Bauchi, Taraba, Ebonyi, Plateau, Benue, Kogi

---

## 🏗️ Pipeline Architecture

```
raw.lassa_cases ──────────────────────────┐
raw.weather ──── staging.weather ─────────┤
raw.population ────────────────────────── mart.lassa_climate ── mart.outbreak_summary
raw.healthcare ────────────────────────────┘
                  staging.lassa_cases ────┘
```

### Asset Layers

| Layer | Asset | Type | Description |
|-------|-------|------|-------------|
| Raw | `raw.lassa_cases` | Python | Lassa cases CSV ingestion |
| Raw | `raw.weather` | Python | Open-Meteo API ingestion |
| Raw | `raw.population` | Python | Population data |
| Raw | `raw.healthcare` | Python | Healthcare infrastructure |
| Staging | `staging.lassa_cases` | DuckDB SQL | Cleans cases, calculates positivity rate |
| Staging | `staging.weather` | DuckDB SQL | Aggregates weather to monthly level |
| Mart | `mart.lassa_climate` | DuckDB SQL | Joins all sources, computes attack rate |
| Mart | `mart.outbreak_summary` | DuckDB SQL | Final summary by state across all years |

---

## ⚙️ Bruin Features Used

- **Python assets** — data ingestion from CSV and REST API
- **SQL assets** — multi-layer transformation (staging → mart)
- **Materialization** — all assets materialize as tables
- **Data quality checks** — not_null, positive, accepted_values on key columns
- **Custom checks** — row count validation on final mart
- **Asset dependencies** — full DAG from raw → staging → mart
- **Bruin MCP** — connected to Claude Code for AI-powered data analysis
- **`bruin ai enhance`** — auto-generated descriptions and quality checks

---

## 🚀 Getting Started

### Prerequisites
- [Bruin CLI](https://getbruin.com/docs/bruin/getting-started/introduction/installation.html)
- Python 3.x
- DuckDB

### Run the pipeline

```bash
# Clone the repo
git clone https://github.com/joskintola/lassa-watch.git
cd lassa-watch

# Run the full pipeline
bruin run . --workers 1

# Validate assets
bruin validate .

# Run quality checks only
bruin run --only checks .
```

---

## 🔍 Key Findings

- **Ebonyi and Kogi** have the highest average CFR (40%+), despite lower case counts — suggesting severe healthcare access gaps
- **Ondo and Edo** consistently account for 50%+ of confirmed cases nationally
- **Seasonal pattern** is clear — cases peak November–April (dry season) correlating with lower humidity
- **Attack rate per 100k** reveals Taraba as disproportionately affected relative to population size

---

## 🛠️ Built With

- [Bruin](https://getbruin.com) — data pipeline orchestration
- [DuckDB](https://duckdb.org) — local analytical database
- [Open-Meteo](https://open-meteo.com) — free weather API
- [NCDC Nigeria](https://ncdc.gov.ng) — epidemiological data source

---

## 📁 Project Structure

```
lassa-watch/
├── .bruin.yml          # Bruin configuration and connections
├── pipeline.yml        # Pipeline definition
├── assets/
│   ├── raw_lassa_cases.py
│   ├── raw_weather.py
│   ├── raw_population.py
│   ├── raw_healthcare.py
│   ├── staging_lassa.sql
│   ├── staging_weather.sql
│   ├── mart_lassa_climate.sql
│   └── mart_outbreak_summary.sql
└── data/
    └── lassa_cases.csv
```

---

*Built for the [Bruin Data Engineering Competition 2026](https://getbruin.com/competition/) — 
```
