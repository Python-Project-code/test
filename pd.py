import pandas as pd
import numpy as np
data = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana",np.nan],
    "Age": [25, 30, 35, 40,np.nan],
    "Gender": ["F", "M", "M", "F",np.nan]
})

print(data)

print(data['Age'].mean())

print(data.isnull().sum())
data = {
    "Name": ["Alice", "Bob", "Alice", "Diana", "Bob"],
    "Age": [25, 30, 25, 22, 30],
    "City": ["New York", "London", "New York", "Paris", "London"]
}
df = pd.DataFrame(data)
print(df)
df_unique = df.drop_duplicates()

unique_count = len(df_unique)

print("DataFrame sin duplicados:")
print(df_unique)
print("\nNúmero de registros únicos:", unique_count)