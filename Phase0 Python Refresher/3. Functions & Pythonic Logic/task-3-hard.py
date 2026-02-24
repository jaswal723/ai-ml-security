# Task - Create a list of dictionaries, where each dictionary is a firewall alert containing a "port" key. Write a single-line list comprehension that returns a new list containing only the alerts where the port is 22 or 3389.

alerts = [
    {"src_ip": "192.168.1.10", "dest_ip": "10.0.0.5", "port": 22, "action": "BLOCK"},
    {"src_ip": "172.16.8.4", "dest_ip": "10.0.0.8", "port": 80, "action": "ALLOW"},
    {"src_ip": "203.0.113.12", "dest_ip": "10.0.0.9", "port": 3389, "action": "BLOCK"},
    {"src_ip": "10.1.1.5", "dest_ip": "10.0.0.6", "port": 443, "action": "ALLOW"},
    {"src_ip": "8.8.8.8", "dest_ip": "10.0.0.10", "port": 53, "action": "ALLOW"}
]
important_alerts = [x for x in alerts if x['port'] in [22,3389]]
print(important_alerts)