def transcription(dna_sequence):
    transcription="" 
    for i in dna_sequence:
        if i == "T":
            transcription+="U"
        elif i =="A":
            transcription+="A"
        elif i == "G":
            transcription+="G"
        elif i == "C":
            transcription+="C"
        
    return transcription

dna_sequence="ATGCGTATGCGCTCTCATGC"

print(transcription(dna_sequence))