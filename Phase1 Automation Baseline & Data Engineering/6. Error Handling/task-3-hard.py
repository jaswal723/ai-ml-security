# Hard: Build a robust wrapper function for a requests.get() API call. 
# Implement a try/except to catch requests.exceptions.Timeout and requests.exceptions.RequestException. 
# If it times out, wait 5 seconds and retry automatically (up to 3 times) before giving up.

import requests
import time
count = 0

while count<3:
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=3)
    except requests.exceptions.Timeout:
        print("Request Timeout.")
        print(f"Retrying... Attempt {count + 1}/3")
        time.sleep(5)
        count+=1
    except requests.exceptions.RequestException:
        print("Request Exception")
        break
    else:
        print(f"Your IP Address: {response.json()['ip']}")
        break
