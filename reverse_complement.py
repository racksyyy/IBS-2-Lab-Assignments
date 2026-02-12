dna="ATGCTGCATTATGCAG"

complements={
    "A":"T",
    "T":"A",
    "C":"G",
    "G":"C"
}

dna_complement="" 
for i in dna:
    dna_complement+=complements[i]

reverse_complement=dna_complement[::-1]

rna=reverse_complement.replace("T","U")

print("Original DNA Sequence:",dna)
print("DNA Complement:",dna_complement)
print("Reverse Complement:",reverse_complement)
print("RNA Sequence:",rna)