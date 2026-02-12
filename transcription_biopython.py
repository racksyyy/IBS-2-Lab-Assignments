from Bio.Seq import Seq

def transcription(dna_sequence):
    dna=Seq(dna_sequence)
    transcription=dna.transcribe()

    return transcription

dna_sequence="ATGCGTAGTGGCTAG"
print("Transcribed RNA Sequence:",transcription(dna_sequence))

