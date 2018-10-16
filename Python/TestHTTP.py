import requests
from time import sleep

url = 'http://192.168.1.28'
payload = {'key1': 'value1', 'key2': 'value2'}

# GET
r = requests.get(url+'/ledOn')

sleep(0.15)

r = requests.get(url+'/ledOff')


# GET with params in URL
#r = requests.get(url, params=payload)

# POST with form-encoded data
#r = requests.post(url, data=payload)

# POST with JSON 
import json
#r = requests.post(url, data=json.dumps(payload))

# Response, status etc
# r.text
# r.status_code