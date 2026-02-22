# Task - Medium: Manually create a small CSV file of firewall logs (Columns: Time, SourceIP, DestIP, Action). Write a script using csv.reader to read the file and print only the rows where Action is "DROP".
import csv
with open("firewall_logs.csv",'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[3] == "DROP":
            print(row)