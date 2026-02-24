# Task - Write a function is_rfc1918(ip) that takes an IP string and returns True if it starts with "10.", "172.", or "192.", and False otherwise.

def is_rfc1918(ip):
    if ip.startswith("10.") | ip.startswith("172.") | ip.startswith("192."):
        return True
    return False
ip = "10.8.9.0"
print(is_rfc1918(ip))