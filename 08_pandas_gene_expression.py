import pandas as pd
data = {
    "Gene" : ["BRCA1","TP53","EGFR","MYC","PTEN","AKT1","VEGFA"],
    "Expression" : [52,85,43,91,35,67,74],
    "Length" : [1863,1182,1210,439,1182,480,2322]
}
df = pd.DataFrame(data)
print(df)
print()

average_length = df["Length"].mean()
average_exp = df["Expression"].mean()
high_exp_gene = df.loc[df["Expression"].idxmax(),"Gene"]
greater_60 = df[df["Expression"] > 60]
sort = df.sort_values(by = "Expression",ascending = False)

print(f"The average length is : {average_length:.4f}")
print()
print(f"The average expression is {average_exp:.4f}")
print()
print(f"The gene with highest expression is : {high_exp_gene}")
print()
print("The genes which are having expression greater than 60 are :")
print(greater_60)
print()
print("The sorted expression from highest to lowest :")
print(sort)
print()
print("Thank You")