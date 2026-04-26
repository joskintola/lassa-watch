"""@bruin
name: raw.weather
type: python
connection: duckdb-default

materialization:
  type: table

@bruin"""

import urllib.request
import json

def materialize():
    states = [
        {"name": "Ondo",    "lat": 7.25,  "lon": 5.20},
        {"name": "Edo",     "lat": 6.34,  "lon": 5.63},
        {"name": "Bauchi",  "lat": 10.31, "lon": 9.84},
        {"name": "Taraba",  "lat": 7.99,  "lon": 10.77},
        {"name": "Ebonyi",  "lat": 6.26,  "lon": 8.01},
        {"name": "Plateau", "lat": 9.22,  "lon": 9.52},
        {"name": "Benue",   "lat": 7.34,  "lon": 8.74},
        {"name": "Kogi",    "lat": 7.80,  "lon": 6.74}
    ]

    rows = []
    for state in states:
        url = (
            f"https://archive-api.open-meteo.com/v1/archive?"
            f"latitude={state['lat']}&longitude={state['lon']}"
            f"&start_date=2021-01-01&end_date=2025-03-31"
            f"&daily=temperature_2m_mean,precipitation_sum,relative_humidity_2m_mean"
            f"&timezone=Africa%2FLagos"
        )
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())

        dates = data['daily']['time']
        temps = data['daily']['temperature_2m_mean']
        precip = data['daily']['precipitation_sum']
        humidity = data['daily'].get('relative_humidity_2m_mean', [None]*len(dates))

        for i in range(len(dates)):
            rows.append({
                'state': state['name'],
                'date': dates[i],
                'temperature_c': temps[i],
                'precipitation_mm': precip[i],
                'humidity_percent': humidity[i]
            })

    return rows