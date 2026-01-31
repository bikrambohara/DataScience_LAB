# Load a CSV file into a DataFrame.
# Display column names, data types, and basic statistics.

import pandas as pd

df = pd.read_csv("Lab5(Pandas)/student.csv")
print(df.info())
print(df.describe())


