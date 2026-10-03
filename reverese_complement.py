seq = input("Enter the DNA  sequence: ").upper()

valid = True

for base in seq:
    if base not in "ATGC":
        valid = False
        break

if valid:
    complement = {
        "A" : "T",
        "T" : "A",
        "G" : "C",
        "C" : "G"
    }

    comp = ""
    for base in seq:
        comp = comp + complement[base]

    rev_comp = comp[::-1]

    print("The original DNA sequence is : ",seq)
    print("The complement of the sequence is : ",comp)
    print("The reverse of the complement is : ",rev_comp)

else:
    print("The DNA sequence is invalid")

print("Thank You")
