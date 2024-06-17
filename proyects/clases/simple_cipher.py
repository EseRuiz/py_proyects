import random

dictionary = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
class Cipher:
    def __init__(self, key=None):
        if key is None:
            self.key =''.join(random.choices('abcdefghijklmnopqrstuvwxyz',k=100))
        else:
            self.key=key

    def encode(self, text):
        lens = []
        lens_text = []
        res = []
        for k in self.key:
            lens.append(dictionary.index(k))
        for txt in text:
            lens_text.append(dictionary.index(txt))
        for i in range(len(text)):
            key_index = i % len(lens)
            sum = lens[key_index] + lens_text[i]
            if sum > 25:
                sum = sum - 26
            res.append(dictionary[sum])
        return ''.join(res)
    
    def decode(self, text):
        lens = []
        lens_text = []
        res = []
        for k in self.key:
            lens.append(dictionary.index(k))
        for txt in text:
            lens_text.append(dictionary.index(txt))
        for i in range(len(text)):
            key_index = i % len(lens)
            sum = lens_text[i] - lens[key_index]
            if sum < 0:
                sum = sum + 26
            res.append(dictionary[sum])
        return ''.join(res)

# cipher = Cipher()
# plaintext = "abcdefghij"
# print(cipher.decode(cipher.encode(plaintext)), plaintext)

# resultado = 10 % 3
# print(resultado)  # Salida: 1
# Aquí, 10 dividido por 3 es igual a 3 con un residuo de 1. Así que 10 % 3 es 1.

# Explicación Paso a Paso
# División Entera:

# Primero se realiza la división entera: 10 // 3 da 3.
# Multiplicación del Cociente por el Divisor:

# Se multiplica el cociente (3) por el divisor (3): 3 * 3 da 9.
# Restar el Producto del Dividendo:

# Finalmente, se resta el producto (9) del dividendo (10): 10 - 9 da 1.