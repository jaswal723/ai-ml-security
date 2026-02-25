# Hard: Load an EDR alert CSV. Filter the DataFrame to only keep rows where the 'Severity' is "High" AND the 'Status' is "New". 
# Update the 'Status' column for those specific rows to "In Progress".

import pandas as pd

df = pd.read_csv(".\\Phase1 Automation Baseline & Data Engineering\\5. Vectorized Filtering\\edr_alerts.csv")
df1 = df.loc[(df.Severity == "High") & (df.Status == "New")]
df1.Status = "In Progress"
print(df1)