# Hard: Combine Week 2 and Week 4.
# Write an API script that queries a threat feed. Configure logging to include timestamps. 
# Log an INFO message when the script starts, 
# a WARNING if an IP returns a high threat score, and an ERROR (with the stack trace) if the API connection drops.

import os
import logging
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("VT-API-KEY")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=".\\Phase1 Automation Baseline & Data Engineering\\7. Enterprise Logging\\task-3.log",
    filemode='w'
)
try:
    response_ipify = requests.get("https://api.ipify.org?format=json")
except:
    logging.error("Something went wrong with the API request to IPIFY.")
else:
    logging.info("The API request to IPIFY was sent successfully.")

if response_ipify.status_code == 200:
    ip = response_ipify.json()['ip']
    print(f"Your IP Address: {ip}")
    logging.info(f"The machine IP Address has been successfully fetched from the IPIFY - {ip}.")
    headers = {
    "x-apikey": api_key,
    "accept": "application/json"
    }
    url = "https://www.virustotal.com/api/v3/ip_addresses/"+ip
    request_vt = requests.get(url, headers=headers)
    logging.info("Request sent to Virustotal API for the IP address.")
    if request_vt.status_code != 200:
        logging.error(f'Error from Virustotal API, Status code - {request_vt.status_code}.')
    else:
        print(f'Malicious Score - {request_vt.json()['data']['attributes']['last_analysis_stats']['malicious']}.')
        logging.info("Execution Complete.")
else:
    logging.error(f"Failed to fetch the current IP address from IPIFY. Response code - {response_ipify.status_code}")