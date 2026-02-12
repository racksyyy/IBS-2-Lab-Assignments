from Bio.Seq import Seq

dna=Seq("ATGTGCTA")

complement=dna.complement()

print("Original DNA sequence: ",dna)
print("Complemengted sequence: ", complement)