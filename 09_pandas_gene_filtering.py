import pandas as pd

data = {
    "Gene": ["BRCA1", "TP53", "EGFR", "MYC", "PTEN", "AKT1", "VEGFA"],
    "Expression": [52, 85, 43, 91, 35, 67, 74],
    "Length": [1863, 1182, 1210, 439, 1182, 480, 2322]
}
 
df = pd.DataFrame(data)
a = df[(df["Expression"] > 60) & (df["Length"] < 1500)]
b = df[(df["Expression"] > 80) | (df["Length"] > 2000)]
c = df.loc[df["Length"].idxmin(),"Gene"]
d = df.loc[df["Length"].idxmax(),"Gene"]
print("The Dataframe is : ")
print(df)
print()

print("The genees where expression is greater than 60 and length is less than 1500: ")
print(a)
print()
print("The genes where expression is greater than 80 and length is greater than 2000 :")
print(b)
print()
print(f"The gene having the minimum length is : {c}")
print()
print(f"The gene having the maximum length is : {d}")