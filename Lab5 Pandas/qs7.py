# Create a new column by transforming Marks(e.g marks/10).
# Rename columns and save the cleaned dataset to CSV file

import pandas as pd

df = pd.read_csv("student4.csv")

df['Marks'] = df['Marks']/10
#Rename columns and save the cleaned dataset to CSV file
df.rename(columns={'Name':'Student Name','Age':'Age of Student','Marks':'Marks/10'}, inplace=True)
df.to_csv("student5.csv", index=False)
print(df)
 