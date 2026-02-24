# Hard: Use csv.DictReader to process a large CSV of authentication logs. Calculate the total number of failed logins per user and write the aggregated results to a brand new CSV using csv.DictWriter.

import csv
log_file=[]
with open(".\Phase1 Automation Baseline & Data Engineering\File Handling & CSVs\\auth_logs.csv","r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        log_file.append(row)
final_dict = {}
for x in log_file:
    if x['Status'] == "Failed":
        if (x['Username'] in final_dict.keys()):
            final_dict[x['Username']]+=1
        else:
            final_dict[x['Username']] = 1
    else:
        pass
final_list = []
for key,value in final_dict.items():
    final_list.append({'Username':key,'FailedLoginCount':value})

with open(".\Phase1 Automation Baseline & Data Engineering\File Handling & CSVs\\auth_logs_failed_results.csv","w",newline = "") as f:
    writer = csv.DictWriter(f,fieldnames=['Username','FailedLoginCount'])
    writer.writeheader()
    writer.writerows(final_list)