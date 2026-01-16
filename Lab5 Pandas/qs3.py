# Select rows where Mrks>60.
# Select only Name and Marks columns

import pandas as pd

df = pd.read_csv("student2.csv")

result = df.loc[df['Marks'] > 60, ['Name', 'Marks']]
print(result)

