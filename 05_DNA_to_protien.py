seq = input("Enter the DNA sequence : ").upper()

valid = True
for base in seq:
    if base not in "ATGC":
        valid = False
        break

if valid:
    codon_table = {
        "TTT": "F", "TTC": "F",
        "TTA": "L", "TTG": "L",

        "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
        "TAT": "Y", "TAC": "Y",
        "TAA": "STOP", "TAG": "STOP",

        "TGT": "C", "TGC": "C",
        "TGA": "STOP", "TGG": "W",

        "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",

        "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",

        "CAT": "H", "CAC": "H",
        "CAA": "Q", "CAG": "Q",

        "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",

        "ATT": "I", "ATC": "I", "ATA": "I",
        "ATG": "M",

        "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",

        "AAT": "N", "AAC": "N",
        "AAA": "K", "AAG": "K",

        "AGT": "S", "AGC": "S",
        "AGA": "R", "AGG": "R",

        "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",

        "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",

        "GAT": "D", "GAC": "D",
        "GAA": "E", "GAG": "E",

        "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"
    }
    protein = ""
    codons = []
    for i in range(0,len(seq) - 2,3):
        codon = seq[i:i+3]
        codons.append(codon)
        amino_acid = codon_table[codon]

        if amino_acid == "STOP":
            break
        protein = protein + amino_acid

    print(f"The DNA sequence is : {seq}")
    print()
    print("Codons : ","|".join(codons))
    print(f"The corresponding amino acid  sequence is : {protein}")
    print()
    print("THANK YOU")
else:
    print("The DNA sequence is not valid")
