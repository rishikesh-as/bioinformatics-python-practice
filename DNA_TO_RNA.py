seq = input("Enter the DNA sequence: ").upper()
valid = True
for base in seq:
    if base not in "ATGC":
        valid = False
        break
if valid:
    RNA = seq.replace("T","U")
    print("The RNA sequence to the corresponding DNA sequence is below: ")
    print()
    print(RNA)

else:
    print("The DNA sequence is invalid")
