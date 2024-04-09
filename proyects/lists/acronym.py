def abbreviate(words):
    res = []
    new_word = words.replace('.','').replace('-',' ').replace('_',' ').split()
    for nw in new_word:
        res.append(nw[0].upper())
    return ''.join(res)

a = abbreviate("Portable Network Graphics")
print(a)