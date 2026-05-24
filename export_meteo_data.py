import requests
import json
from datetime import datetime
import os

# Configuration
DIR_METEO_DATA = r"C:\Users\katia\OneDrive\Documents\meteo_elt\data"

# extract meteo daily data
response = requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m')
if response.status_code == 200:
    temperature_data = response.json()
    print(temperature_data)
    print('SUCCESS')
else:
    print(f'ERROR CODE: {response.status_code} : {response.reason}')

# load meteo daily data
metadata_open_meteo = {
    "elt_timestamp" : datetime.now().isoformat(),
    "elt_source_API" : "Open Meteo API",
    "elt_data_API" : temperature_data 
}

# store JSON meteo daily data into a file
file_path = os.path.join(DIR_METEO_DATA, f'meteo_daily_data.json')
os.makedirs(DIR_METEO_DATA, exist_ok = True)
with open(file_path,'w') as f:
    json.dump(metadata_open_meteo, f, indent=4)

print(f'JSON daily meteo data has been stored in {file_path}')