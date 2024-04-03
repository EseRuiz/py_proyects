def rows(letter):
    diamond = []
    diamonds = []
    dictionary = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    length = dictionary.index(letter.lower())+1
    for let in range(length):
        if let == 0:
            diamond.append((length-1)*' ' + dictionary[let].upper() + (length-1)*' ')
        elif let > 0:
            diamond.append((length-let-1)*' ' + dictionary[let].upper() + ((2*let)-1)*' ' + dictionary[let].upper() + (length-let-1)*' ')
    diamonds = diamond[::-1][1:]
    return (diamond + diamonds)
a = rows("D")
print(a)