import numpy as np
sample_A = np.array([10,20,30,40,50])
sample_B = np.array([15,18,35,38,55])

difference = sample_B - sample_A
average = (sample_A + sample_B) / 2
higher_B = sample_B[sample_B > sample_A]
largest_increase = np.max(difference)
print(f"Sample A is : {sample_A}")
print(f"Sample B is : {sample_B}")
print(f"The difference between two samples (A-B) is : {difference}")
print(f"The average is : {average}")
print(f"The values higher in Sample B is {higher_B}")
print(f"The largest increase is : {largest_increase}")
