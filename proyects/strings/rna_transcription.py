def to_rna(dna_strand):
    rna_final = []
    for rna in dna_strand:
        if rna_final == "":
            return ""
        if rna == 'G':
            rna_final.append('C')
        if rna == 'C':
            rna_final.append('G')
        if rna == 'T':
            rna_final.append('A')
        if rna == 'A':
            rna_final.append('U')
    return "".join(rna_final)

a = to_rna("ACGTGGTCTTAA")
print(a)
