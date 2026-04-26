"""@bruin

name: raw.lassa_cases
connection: duckdb-default

materialization:
  type: table

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
  - name: state_share_percent
    type: DOUBLE

@bruin"""

import csv
import os

def materialize():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, "data", "lassa_cases.csv")
    
    rows = []
    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append({
                'year': int(row['year']),
                'state': row['state'],
                'suspected_cases': int(row['suspected_cases']),
                'confirmed_cases': int(row['confirmed_cases']),
                'deaths': int(row['deaths']),
                'cfr_percent': float(row['cfr_percent']),
                'state_share_percent': float(row['state_share_percent'])
            })
    return rows
