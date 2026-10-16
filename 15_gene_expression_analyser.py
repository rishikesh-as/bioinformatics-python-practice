import numpy as np
import pandas as pd

data = {
    "Gene": ["BRCA1", "TP53", "EGFR", "MYC", "PTEN",
             "AKT1", "VEGFA", "KRAS"],
    "Expression": [52, 85, 43, 91, 35, 67, 74, 58],
    "Length": [1863, 1182, 1210, 439, 1182, 480, 2322, 189],
    "Condition": ["Normal", "Tumor", "Normal", "Tumor",
                  "Normal", "Tumor", "Tumor", "Normal"]
}

df = pd.DataFrame(data)

print("Gene Expression Dataset")
print(df)
print()

avg_exp = df["Expression"].mean()
print(f"The Average gene expression is {avg_exp}")
print()

max_exp = df["Expression"].max()
print(f"The maximum Gene expression is {max_exp}")
print()

min_exp = df["Expression"].min()
print(f"The minimum Gene Expression is {min_exp}")
print()

avg_len = df["Length"].mean()
print(f"The average length is {avg_len}")
print()

high_exp = df.loc[df["Expression"].idxmax(),"Gene"]
print(f"The gene having the highest expression is {high_exp}")
print()

low_exp = df.loc[df["Expression"].idxmin(),"Gene"]
print(f"The gene having the lowest expression is {low_exp}")
print()

high_exp_gene = df[df["Expression"] > 70]
print("The genes with expression greater than 70 are : ")
print(high_exp_gene)
print()

conditions = [
    df["Expression"] >= 80,
    (df["Expression"] >= 50) & (df["Expression"] < 80)
]

choices = ["High","Medium"]

df["Expression_level"] = np.select(
    conditions,
    choices,
    default = "Low"
)

print("DataFrame with Expression level")
print(df)
print()

df["Expression_level"] = pd.Categorical(
    df["Expression_level"],
    categories = ["High","Medium","Low"],
    ordered = True
)

df_sort = df.sort_values(by = "Expression_level")
print("The DataFrame sorted accorging to Expression Level")
print(df_sort)
print()

avg_by_condition = df.groupby("Condition")["Expression"].mean() 
print("The Average Gene Expression of normal and tumor genes are ")
print(avg_by_condition)
print()

#Finding highest average gene expression
high_avg = avg_by_condition.idxmax()
print(f"The condition with highest gene expression is {high_avg}")
print()

#Enter the gene name and get the information about that particular gene.
gene_name = input("Enter the name of the gene : ").upper()
result = df[df["Gene"] == gene_name]

if result.empty:
    print("Gene not found")
else:
    print(result)

#To get the output according to the normal and tumor conditions
con = input("Enter the condition(Normal or Tumor) : ").strip().capitalize()
res = df[df["Condition"] == con]

if res.empty:
    print("Invalid entry.")
    print()
else:
    print(res)
    print()

#Sorting the Dataframe in ascending order according to the gene expression
sort = df.sort_values(by = "Expression",ascending = True)
print(sort)