dictionary =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
atbash_dict = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
def encode(plain_text):
    plain_text_espaces = plain_text.replace(' ','').replace('.','').replace(',','')
    convert = [wr.lower() for wr in plain_text_espaces]
    new = []
    count = 0
    final = ""
    for word in range(len(plain_text_espaces)):
        if convert[word].isnumeric() :
            new.append(convert[word])
        else:
            new.append(atbash_dict[dictionary.index(convert[word])])

    for new_word in new:
        if count == 5:
            final += " "
            count = 0
        final += new_word
        count += 1    

    return final

def decode(ciphered_text):
    plain_text_espaces = ciphered_text.replace(' ','').replace('.','').replace(',','')
    convert = [wr.lower() for wr in plain_text_espaces]
    new = []
    for word in range(len(plain_text_espaces)):
        if convert[word].isnumeric() :
            new.append(convert[word])
        else:
            new.append(atbash_dict[dictionary.index(convert[word])])
    return ''.join(new)
a = encode("Testing,1 2 3, testing.")
b = decode("vc vix    r hn")
print(b)