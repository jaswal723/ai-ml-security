# Hard: You have two CSVs: scans.csv (IP, Vulnerability) and assets.csv (IP, Owner). 
# Load both into DataFrames. Use pd.merge() to join them on the IP address column so you have a single table showing the Vulnerability and the Owner, then export it to a new CSV.

import pandas as pd

df1 = pd.read_csv(".\\Phase1 Automation Baseline & Data Engineering\\4. Pandas DataFrames\\scans.csv")
df2 = pd.read_csv(".\\Phase1 Automation Baseline & Data Engineering\\4. Pandas DataFrames\\assets.csv")
newdf = pd.merge(df1,df2,on='IP',how='outer')
print(newdf)