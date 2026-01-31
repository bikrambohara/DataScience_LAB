# Check for missing values in the dataset.
# Fill missing numerical Values with the mean

import pandas as pd

df = pd.read_csv("Lab5(Pandas)/student3.csv")


print("Missing values in the column")
print(df.isnull().sum())

# new_df = df.dropna()
# print(new_df.to_string())

df.fillna(df.mean(numeric_only=True), inplace=True)
print(df.to_string())

