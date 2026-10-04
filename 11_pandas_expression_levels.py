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
print("The dataframe is : ")
print(df)

conditions = [
    df["Expression"] >= 80,
    (df["Expression"] >= 50) & (df["Expression"] < 80)
]
choices = [
    "High",
    "Medium"
]
df["Expression_level"] = np.select(
    conditions,
    choices,
    default = "Low"
)
print()
print(df)
count_gene = df.groupby("Expression_level")["Gene"].count()
print()
print("The number of genes in each choices : ")
print(count_gene)

high_gene = df[df["Expression_level"] == "High"]["Gene"]
print()
print("The genes which are having higher expression:")
print(high_gene)

avg_high = df[df["Expression_level"] == "High"]["Expression"].mean()
print()
print("The average expression of highly expressing gene : ",avg_high)

