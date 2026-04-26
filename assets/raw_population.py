"""@bruin
name: raw.population
type: python
connection: duckdb-default

materialization:
  type: table

@bruin"""

def materialize():
    # Population estimates from NBS Nigeria / WorldPop
    return [
        {"state": "Ondo",   "population": 4112000},
        {"state": "Edo",    "population": 4235000},
        {"state": "Bauchi", "population": 7150000},
        {"state": "Taraba", "population": 3066000},
        {"state": "Ebonyi", "population": 2880000},
        {"state": "Plateau","population": 4200000},
        {"state": "Benue",  "population": 5740000},
        {"state": "Kogi",   "population": 4470000}
    ]