# Easy: Load a firewall log CSV into a DataFrame. 
# Create a new DataFrame that only contains rows where the 'DestinationPort' is 443.

import pandas as pd

df = pd.read_csv(".\\Phase1 Automation Baseline & Data Engineering\\5. Vectorized Filtering\\firewall_logs.csv")
final_df = df[df['DestinationPort'] == 443]
print(final_df)