def distance(strand_a, strand_b):
    differences = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    if len(strand_a) == len(strand_b):
        seta = [letter for letter in strand_a]
        setb = [lette2 for lette2 in strand_b]
        for i in range(len(setb)):
            if seta[i] != setb[i]:
                differences += 1
        return differences
    #TODO preguntar porque al medir la len de una lista y restarle uno aumenta y cual es
    #la diferencia con el len de un set o un dic
    
#a = distance("ATA", "AGTG")
#print(a)
###
      #  for a, b in zip(strand_a, strand_b):
      #  if a != b:
      #      differences += 1
    