# identify outliers in the marks column using the IQR method.
#Remove the outliers from the dataset

import pandas as pd

df = pd.read_csv("student4.csv")

Q1 = df['Marks'].quantile(0.25)
Q3 = df['Marks'].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[(df['Marks'] < lower_limit) | (df['Marks'] > upper_limit)]
print(outliers)

# Remove outliers
df = df[(df['Marks'] >= lower_limit) & (df['Marks'] <= upper_limit)]
print("AFTER REMOVING OUTLIERS")
print(df)
