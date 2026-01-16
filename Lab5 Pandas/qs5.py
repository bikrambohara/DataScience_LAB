# Detect duplicate rows in the dataset.
# Remove duplicate and verify the result

import pandas as pd

df = pd.read_csv("student4.csv")
print(df.duplicated())

df.drop_duplicates(inplace=True)
print(df.to_string())

