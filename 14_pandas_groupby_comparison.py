import pandas as pd
data = {
    "Gene": ["BRCA1", "TP53", "EGFR", "MYC", "PTEN", "AKT1", "VEGFA", "KRAS"],
    "Expression": [52, 85, 43, 91, 35, 67, 74, 58],
    "Length": [1863, 1182, 1210, 439, 1182, 480, 2322, 189],
    "Condition": ["Normal", "Tumor", "Normal", "Tumor",
                  "Normal", "Tumor", "Tumor", "Normal"]
}
df = pd.DataFrame(data)
print("The old DataFrame is :  ")
print(df)
print()

avg_exp = df.groupby("Condition")["Expression"].mean()
print("The Average Expression for Normal and Tumor genes are : ")
print(avg_exp)
print()

avg_length = df.groupby("Condition")["Length"].mean()
print("The Average Length for Normal and Tumor genes are : ")
print(avg_length)
print()

max_exp = df.groupby("Condition")["Expression"].max()
print("The Maximum Expression for Normal and Tumor genes are : ")
print(max_exp)
print()

count_genes = df.groupby("Condition")["Gene"].count()
print("The number of genes belonging to each conditions are : ")
print(count_genes)
print()

high_exp = avg_exp.idxmax()
print("The Condition having higher Average Expression is : ",high_exp)

