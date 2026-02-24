# Medium: Use the free AlienVault OTX API or Abuse.ch API. Send a GET request to pull their recent indicators. 
# Parse the response.json() and print the top 5 most recent malicious IP addresses.

import os
import requests
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("OTX-API-KEY")
headers = {
    "X-OTX-API-KEY": api_key
}
request = requests.get("https://otx.alienvault.com/api/v1/pulses/602bc528f447d628d41494f2/indicators", headers=headers)
final_5_ips = []
if request.status_code != 200:
    print(f'Error, Status code - {request.status_code}')
else:
    response = request.json()
    ip_list = response['results']
    i=0
    j=0
    while i<5:
        if ip_list[j]['type'] == "IPv4":
            final_5_ips.append(ip_list[j])
            j+=1
            i+=1
        elif j>=100:
            print("Error, limit crossed")
        else:
            j+=1
for x in final_5_ips:
    print(x['indicator'])
