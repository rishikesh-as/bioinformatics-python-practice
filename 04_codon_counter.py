seq = input("Enter the DNA sequence : ").upper()

valid = True

for base in seq:
    if base not in "ATGC":
        valid = False
        break

if valid:
    codon_count = {}
    for i in range(0,len(seq) - 2,3):

        codon = seq[i:i+3]

        if codon in codon_count:
            codon_count[codon] = codon_count[codon] + 1
        else:
            codon_count[codon] = 1

    print("CODON COUNTS")
    for codon in codon_count:
        print(f"{codon} : {codon_count[codon]}")
else:
    print("The DNA sequence is invalid")