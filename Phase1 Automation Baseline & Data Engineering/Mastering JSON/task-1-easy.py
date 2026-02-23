# Task - Easy: Create a Python dictionary representing a malware sandbox report. Use json.dumps() to print it to the console as a nicely formatted JSON string (use the indent=4 parameter).
import json
malware_sandbox_report = {
    "file_name": "invoice_update.exe",
    "file_hash": "a84f3c29d0b5a9e7f91e20c0dfbc12c3",
    "threat_score": 9.2,
    "behavior_tags": ["keylogging", "network_beaconing", "persistence"],
    "contacted_domains": ["malicious-server.biz", "c2-control.net"],
    "signature": {
        "vendor": "Any.Run",
        "verified": False
    }
}
report_json = json.dumps(malware_sandbox_report,indent=4)
print(report_json) 