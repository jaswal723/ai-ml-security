# Medium: Load a CSV of Active Directory users. 
# Select only the columns SamAccountName and LastLogonDate. 
# Drop any rows that have missing (NaN) values using .dropna(), and print the result.

import pandas as pd

df = pd.read_csv(".\\Phase1 Automation Baseline & Data Engineering\\4. Pandas DataFrames\\active_directory_users.csv",usecols= ['SamAccountName','LastLogonDate'])
newdf = df.dropna()
print(newdf)