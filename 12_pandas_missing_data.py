import numpy as np
import pandas as pd
data = {
    "Gene": ["BRCA1", "TP53", "EGFR", "MYC", "PTEN", "AKT1", "VEGFA", "KRAS"],
    "Expression": [52, 85, np.nan, 91, 35, np.nan, 74, 58],
    "Length": [1863, 1182, 1210, np.nan, 1182, 480, 2322, 189],
    "Condition": ["Normal", "Tumor", "Normal", "Tumor",
                  "Normal", "Tumor", "Tumor", "Normal"]
}
df = pd.DataFrame(data)
print(df)
print()

print("Where are the missing values :  ")
print(df.isna())
print()

print("The rows containing missing values are : ")
print(df[df.isna().any(axis = 1)])
print()

missing_count = df.isna().sum()
print("Missing values in each column: ")
print(missing_count)
print()

total_missing = df.isna().sum().sum() 
print("Total number of missing values : ",total_missing)
print()

average_expression = df["Expression"].mean()
df["Expression"] = df["Expression"].fillna(average_expression)

average_length = df["Length"].mean()
df["Length"] = df["Length"].fillna(average_length)

print("DataFrame after filling missing values: ")
print(df)
