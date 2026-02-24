# Task - Write a function calculate_severity(cvss_score) that takes a float. Return "Critical" for 9.0+, "High" for 7.0-8.9, etc. Test it with several inputs.

def calculate_severity(cvss_score):
    if cvss_score >= 9.0:
        return "Critical"
    elif cvss_score >= 7.0:
        return "High"
    elif cvss_score >= 4.0:
        return "Medium"
    elif cvss_score >= 0.1:
        return "Low"
    else:
        return "None"
cvss_score = 8.5
print(calculate_severity(cvss_score))