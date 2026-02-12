def complement(dna_sequence):
    complement="" 
    for base in dna_sequence:
        if base == 'A':
            complement += 'T'
        elif base == 'T':
            complement += 'A'
        elif base == 'C':
            complement += 'G'  
        elif base == 'G':
            complement += 'C'
    return complement

dna_sequence = "ACGTACGTACGT"
print(complement(dna_sequence))