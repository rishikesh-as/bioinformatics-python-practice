import pandas as pd
data = {
    "Gene": ["BRCA1", "TP53", "EGFR", "MYC", "PTEN", "AKT1", "VEGFA", "KRAS"],
    "Expression": [52, 85, 43, 91, 35, 67, 74, 58],
    "Length": [1863, 1182, 1210, 439, 1182, 480, 2322, 189],
    "Condition": ["Normal", "Tumor", "Normal", "Tumor",
                  "Normal", "Tumor", "Tumor", "Normal"]
}

df = pd.DataFrame(data)
average_expression = df.groupby("Condition")["Expression"].mean()
average_length = df.groupby("Condition")["Length"].mean()
max_expression = df.groupby("Condition")["Expression"].max()
count = df.groupby("Condition")["Gene"].count()
highest_average_condition = average_expression.idxmax()

print("The Dataframe is : ")
print(df)
print()

print("Average expression for each condition: ")
print(average_expression)
print()

print("Average length for each condition : ")
print(average_length)
print()

print("Maximum expression for each condition : ")
print(max_expression)
print()

print("Condition with the highest average expression:")
print(highest_average_condition)
print()

print("Number of genes present in each condition : ")
print(count)