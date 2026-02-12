def translation_rna_to_protein(rna_sequence):
    codon_table = {
    "UUU": "F", "UUC": "F", "UUA": "L",
    "UUG": "L", "CUU": "L", "CUC": "L",
    "CUA": "L", "CUG": "L", "AUU": "I",
    "AUC": "I", "AUA": "I", "AUG": "M",
    "GUU": "V", "GUC": "V", "GUA": "V",
    "GUG": "V", "UCU": "S", "UCC": "S",
    "UCA": "S", "UCG": "S", "AGU": "S",
    "AGC": "S", "CCU": "P", "CCC": "P",
    "CCA": "P", "CCG": "P", "ACU": "T",
    "ACC": "T", "ACA": "T", "ACG": "T",
    "GCU": "A", "GCC": "A", "GCA": "A",
    "GCG": "A", "UAU": "Y", "UAC": "Y",
    "CAU": "H", "CAC": "H", "CAA": "Q",
    "CAG": "Q", "AAU": "N", "AAC": "N",
    "AAA": "K", "AAG": "K", "GAU": "D",
    "GAC": "D", "GAA": "E", "GAG": "E",
    "UGU": "C", "UGC": "C", "UGG": "W",
    "CGU": "R", "CGC": "R", "CGA": "R",
    "CGG": "R", "AGA": "R", "AGG": "R",
    "GGU": "G", "GGC": "G", "GGA": "G",
    "GGG": "G", "UAA": "*", "UAG": "*",
    "UGA": "*"
    }

    protein_sequence="" 
    for i in range(0, len(rna_sequence),3):
        codon=rna_sequence[i:i+3]
        amino_acid=codon_table.get(codon, 'X')
        if amino_acid=='*':
            break
        protein_sequence+=amino_acid

    return protein_sequence


rna_sequence="AUGCGUAGCGCUAGCAGCUAUCGUAC"
protein_sequence=translation_rna_to_protein(rna_sequence)

print("RNA Sequence:",rna_sequence)
print("Protein Sequence:",protein_sequence)