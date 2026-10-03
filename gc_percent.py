seq = input("Enter the sequence : ").upper()
length = len(seq)
A = seq.count("A")
T = seq.count("T")
G = seq.count("G")
C = seq.count("C")

GC_percent = ((G+C) / length) * 100.0

valid = True
for base in seq:
    if base not in "ATGC":
        valid = False
        break

print("The length of the DNA sequence is : ",length)
print()
print("The number of Adenine(A) is : ",A)
print("The number of Thymine(T) is : ",T)
print("The number of Guanine(G) is : ",G)
print("The number of Cytosine(C) is : ",C)
print()
print(f"The GC percentage in the DNA sequence is : {GC_percent:.4f}")

if valid:
    print("The DNA sequence is valid.")
else:
    print("The DNA sequence is not valid.It contains invalid characters.")