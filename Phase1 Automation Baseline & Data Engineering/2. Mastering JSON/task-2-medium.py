# Task - Medium: Save a sample JSON payload from an AWS CloudTrail alert to a local file. Write a script to json.load() the file and print the userName and eventName.
import json
with open(".\Phase1 Automation Baseline & Data Engineering\Mastering JSON\cloudtrail_alert.json",'r') as f:
    alert_log = json.load(f)
    print(f'Username: {alert_log['userIdentity']['userName']}')
    print(f'Eventname: {alert_log['eventName']}')