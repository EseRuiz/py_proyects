amino_acids = {
    "Methionine": ["AUG"],
    "Phenylalanine": ["UUU", "UUC"],
    "Leucine": ["UUA", "UUG"],
    "Serine": ["UCU", "UCC", "UCA", "UCG"],
    "Tyrosine": ["UAU", "UAC"],
    "Cysteine": ["UGU", "UGC"],
    "Tryptophan": ["UGG"],
    "STOP": ["UAA", "UAG", "UGA"]
}
def proteins(strand):
    expect1 = []
    expect = []
    new_strand = ""
    list_strand = []
    count = 0
    for amino in strand:
        if count == 3:
            list_strand.append(new_strand)
            new_strand = ""
            count = 0
        new_strand += amino
        count += 1
    if new_strand:
        list_strand.append(new_strand)

    for amino_lis in list_strand:
        for a , lis in amino_acids.items():
            if amino_lis in lis:
                expect.append(a)

    for esp in expect:
        if esp == 'STOP':
            return expect1
        expect1.append(esp) 

    
    return expect1

a = proteins("UGGUAGUGG")
print(a)
