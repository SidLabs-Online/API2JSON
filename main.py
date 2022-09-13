import requests
import json

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").text

#print(response)

response_stacked = json.loads(response)

#print(response_stacked)
#print(type(response_stacked))

print(response_stacked['time'])

