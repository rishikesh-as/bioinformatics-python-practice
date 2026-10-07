import numpy as np
import pandas as pd
data = {
    "Gene": ["BRCA1", "TP53", "EGFR", "MYC", "PTEN", "AKT1", "VEGFA", "KRAS"],
    "Expression": [52, 85, 43, 91, 35, 67, 74, 58],
    "Length": [1863, 1182, 1210, 439, 1182, 480, 2322, 189],
    "Condition": ["Normal", "Tumor", "Normal", "Tumor",
                  "Normal", "Tumor", "Tumor", "Normal"]
} 
df = pd.DataFrame(data)
print("The old DataFrame is : ")
print(df)
print()

a = df[(df["Expression"] >= 60) & (df["Length"] < 1500)]
print("The genes which have Expression greater than or equal to 60 and Length less than 1500 are : ")
print(a)
print()

b = df[(df["Expression"] >= 80) | (df["Length"] > 2000)]
print("The genes with Expression greater than or equal to 80 or Length greater than 2000 are : ")
print(b)
print()

conditions = [
    df["Expression"] >= 80,
    (df["Expression"] >= 50) & (df["Expression"] <80)
]

choices = ["High","Medium"]

df["Expression_level"] = np.select(
    conditions,
    choices,
    default = "Low"
)

print("The DataFrame with the new row Expression level is : ")
print(df)