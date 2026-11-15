import requests

response = requests.get('https://boards-api.greenhouse.io/v1/boards/hootsuite/jobs?clecontent=true')
data = response.json()
print(data["meta"]["total"])
print(len(data["jobs"]))