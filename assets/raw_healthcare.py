"""@bruin
name: raw.healthcare
type: python
connection: duckdb-default
materialization:
  type: table

@bruin"""

def materialize():
    # NBS Nigeria health facility data + Lassa Treatment Centres (LTCs) from NCDC
    return [
        {"state": "Ondo",    "hospitals": 42, "lassa_treatment_centres": 3, "health_workers_per_10k": 18},
        {"state": "Edo",     "hospitals": 55, "lassa_treatment_centres": 4, "health_workers_per_10k": 22},
        {"state": "Bauchi",  "hospitals": 38, "lassa_treatment_centres": 2, "health_workers_per_10k": 9},
        {"state": "Taraba",  "hospitals": 21, "lassa_treatment_centres": 1, "health_workers_per_10k": 7},
        {"state": "Ebonyi",  "hospitals": 18, "lassa_treatment_centres": 1, "health_workers_per_10k": 8},
        {"state": "Plateau", "hospitals": 34, "lassa_treatment_centres": 2, "health_workers_per_10k": 14},
        {"state": "Benue",   "hospitals": 29, "lassa_treatment_centres": 1, "health_workers_per_10k": 10},
        {"state": "Kogi",    "hospitals": 27, "lassa_treatment_centres": 1, "health_workers_per_10k": 11}
    ]