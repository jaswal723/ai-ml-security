# Hard: Write a script that takes a list of 5 file hashes. 
# Loop through them and send a GET request to the VirusTotal API for each. 
# You must successfully pass your API key in the request headers (not in the URL), extract the malicious hit count from the complex JSON response, and print it.

import os
import requests
import time
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("VT-API-KEY")
hashes = [
    "03a35f49b8ccd13cb1f47822cc23b547b01cd8b4f4a0b54d3ec34d6ba2c5b7cf",
    "a46bee5cf4a75e8c909a2ba10879e2b50a03c3c314d203c2fb507982ed62f7e0",
    "dcb76db87a9aba556162e1c572ba6b9321bfc422bbffeff8209aaac7e5280098",
    "852ff4f0970518ebf1c5e2bbb70574b11c9e52439fa22ab8a7f124614f7c4ba7",
    "d24e5960b9ce0ba4a053ac20f68d06ea"
]
headers = {
    "x-apikey": api_key,
    "accept": "application/json"
}

for x in hashes:
    url = "https://www.virustotal.com/api/v3/files/"+x
    request = requests.get(url, headers=headers)
    if request.status_code != 200:
        print(f'Error, Status code - {request.status_code}')
    else:
        print(f'File Hash - {x}')
        print(f'Malicious Score - {request.json()['data']['attributes']['last_analysis_stats']['malicious']}\n')
    time.sleep(20)
