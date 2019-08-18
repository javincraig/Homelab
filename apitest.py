import requests
import json

url = 'http://192.168.0.104:32768/api/'
username = 'admin'
password = 'admin'
response = requests.get(f'{url}dcim/sites/', verify=False, auth=(username, password))

resp_dict = (json.loads(response.text))

for i in resp_dict['results']:
    if i['shipping_address'] == '':
        print(i)