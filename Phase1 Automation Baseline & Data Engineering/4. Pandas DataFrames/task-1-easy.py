# Easy: Download a sample CSV of network traffic. 
# Load it into a Pandas DataFrame using pd.read_csv() and print the first 10 rows using .head(10)

import pandas as pd

df = pd.read_csv(".\\Phase1 Automation Baseline & Data Engineering\\4. Pandas DataFrames\\network_traffic.csv")
print(df.head(10))