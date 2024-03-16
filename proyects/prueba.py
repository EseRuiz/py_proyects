def prueba(oracion):
    palabras = oracion.split()
    palabras2 = {word:len(word) for word in palabras}
    palabras2_ordenadas = dict(sorted(palabras2.items(), key=lambda item: item[1]))
    return (' '.join(palabras2_ordenadas.keys()))

a = prueba("catss and dogs airplane")
print(a)
