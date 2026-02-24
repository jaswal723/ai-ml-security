# Task - Hard: Take a deeply nested JSON file representing a complex EDR process tree. Write a recursive function that searches through the entire JSON structure and extracts all unique MITRE ATT&CK technique IDs (e.g., "T1059") into a Python set.

import json

def extract_techniques(reader_file,final_list):
    for x in reader_file:
        for y in x['techniques']:
            final_list.append(y)
        if len(x['children']) != 0:
            extract_techniques(x['children'],final_list)
    return


with open(".\\Phase1 Automation Baseline & Data Engineering\\Mastering JSON\\edr_process_tree.json",'r') as f:
    reader_file = json.load(f)

final_list = []
for x in reader_file["techniques"]:
    final_list.append(x)

if len(reader_file['children']) != 0:
    extract_techniques(reader_file['children'],final_list)
print(set(final_list))
 