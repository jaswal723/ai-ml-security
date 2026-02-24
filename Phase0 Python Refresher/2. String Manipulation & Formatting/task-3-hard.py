# Task - Write a script that takes a multiline string of raw HTTP headers, splits them by line, and parses them into a Python dictionary where the header name is the key and the value is the header value.

headers = """Host: suspicious-domain.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
Accept: text/html,application/xhtml+xml
Referer: http://malicious-site.biz/phish
Connection: keep-alive
X-Forwarded-For: 192.168.1.100"""
headers_new_line = headers.split('\n')
headers_dict = {}
for x in headers_new_line:
    y = x.split(': ',maxsplit=1)
    headers_dict[y[0]] = y[1]
print(headers_dict)
