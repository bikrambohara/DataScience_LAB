# 1. Import pandas and create a DataFrame with columns: Name, Age, Marks.
# Display the first 5 rows and dataset shape.

import pandas as pd

data = {
    "Name": ["Nikhil", "Bikram", "Mandip", "Ayush", "Rahul", "Shaurya", "Nakhil", "Kritika","Shita","Ravi","Ram"],
    "Age": [25, 22, 19, 27, 23, 20, 24, 21, 25, 22, 19],
    "Marks": [85, 92, 78, 90, 85, 92, 78, 90, 85, 92, 78]
}
df = pd.DataFrame(data)
print(df.head())
print(df.shape)
