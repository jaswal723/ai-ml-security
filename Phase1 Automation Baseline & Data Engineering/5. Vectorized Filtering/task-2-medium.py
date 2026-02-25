# Medium: Using a proxy log DataFrame, use .value_counts() on the 'Domain' column to instantly print the top 10 most visited websites in the dataset.

import pandas as pd

df = pd.read_csv(".\\Phase1 Automation Baseline & Data Engineering\\5. Vectorized Filtering\\proxy_logs.csv")
print(df.Domain.value_counts())