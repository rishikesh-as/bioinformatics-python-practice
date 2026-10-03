import numpy as np
expression = np.array([12, 18, 25, 10, 35, 22, 17, 40, 28, 15])
print("Mean = ",round(np.mean(expression),4))
print("Median = ",round(np.median(expression),4))
print("Maximum = ",np.max(expression))
print("Minimum = ",np.min(expression))
print("Standard Deviation = ",round(np.std(expression),4))
big = expression[expression > 20]
count = len(big)
percent = (count / len(expression)) * 100
print("The values greater than 20 is : ",big)
print("The percentage is : ",percent)