# Task - Easy: Write a script that creates a text file called suspect_domains.txt and writes three malicious URLs into it using Python.

malicious_urls = ["www.mal-url-1.com","www.mal-url-2.com","www.mal-url-3.com"]
with open("suspect_domains.txt","w") as f:
    f.writelines(x + "\n" for x in malicious_urls)