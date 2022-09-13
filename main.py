import requests
import json

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()

print(response)

#response_stacked = json.loads(response)

#print(response_stacked)
#print(type(response_stacked))

# for keys, values in response_stacked:
#   print(keys, ":", values)