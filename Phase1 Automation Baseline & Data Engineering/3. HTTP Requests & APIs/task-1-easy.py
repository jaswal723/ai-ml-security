# Easy: Write a script that makes a GET request to https://api.ipify.org?format=json and prints your current public IP address.

import requests

response = requests.get("https://api.ipify.org?format=json")
if response.status_code != 200:
    print(f'Error, Status code: {response.status_code}')
else:
    ip_response = response.json()
    print(f"Your IP Address: {ip_response['ip']}")