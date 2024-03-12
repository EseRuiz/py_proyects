def two_fer(name=None): #valor por defecto name=None para poder comparar
    if name is None:
        return ("One for you, one for me.")
    return ("One for "+name+", one for me.")

a= two_fer()
print(a)
