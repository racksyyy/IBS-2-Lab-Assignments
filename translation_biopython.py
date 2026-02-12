from Bio.Seq import Seq

def translation(rna_sequence):
    rna=Seq(rna_sequence)

    protein_sequence=rna.translate()
    return protein_sequence

rna_sequence="AUGGUGGGAGAUAUGCCGAGC"

print("RNA sequence:",rna_sequence)
print("Protein sequence:",translation(rna_sequence))