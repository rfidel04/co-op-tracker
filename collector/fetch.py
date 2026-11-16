import requests
import json
import datetime

response = requests.get('https://boards-api.greenhouse.io/v1/boards/hootsuite/jobs?content=true')
data = response.json()

date = datetime.date.today()
path= f"data/raw/hootsuite_{date}.json"

with open(path,"w") as f:
    json.dump(data, f)
print(data["meta"]["total"])
print(len(data["jobs"]))