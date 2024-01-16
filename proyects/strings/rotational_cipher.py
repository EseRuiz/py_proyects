def rotate(text, key):
    pos = []
    new_text = [letter for letter in text]
    dictionary = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in new_text:
        if i.isalpha():#isnumeric()
            if i != dictionary[dictionary.index(i.lower())].upper():
                if dictionary.index(i)+key >= 26:
                    pos.append(dictionary[abs(26-dictionary.index(i)-key)])
                else:pos.append(dictionary[dictionary.index(i)+key])
            elif i == dictionary[dictionary.index(i.lower())].upper():
                if dictionary.index(i.lower())+key >= 26:
                    pos.append(dictionary[abs(26-dictionary.index(i.lower())-key)].upper())
                else:pos.append(dictionary[dictionary.index(i.lower())+key].upper())
        else:
            pos.append(i)
    result = ''.join([res for res in pos])
    return str(result)
