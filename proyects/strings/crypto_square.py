import re

def cipher_text(plain_text):
    res = []
    texto_normalizado = re.sub(r'[^a-zA-Z0-9]', '', plain_text).lower()
    length = len(texto_normalizado)
    
    if length == 0:
        return ''

    c = 0
    while c * c < length:
        c += 1
    r = c - 1 if c * (c - 1) >= length else c

    texto_normalizado += ' '*((c*r)-length)
    for i in range(c):
        res.append(texto_normalizado[i::c])
    return ' '.join(res)

a = cipher_text("This is fun!")
print(a)