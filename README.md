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

**Stat
