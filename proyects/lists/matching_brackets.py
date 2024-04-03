def is_paired(input_string):
    count = []
    open = "([{"
    close = ")]}"
    for chr in input_string:
        if chr in open:
            count.append(chr)
        elif chr in close:
            if not count or open.index(count.pop()) != close.index(chr):
                return False
    return not count

"""
    si se tiene "({}{}{})" el ira agregando a la lista count los caracteres de open "([{" si llega a un caracter de close ")]}"
    el toma ese caracter y lo elimina de la listay lo examina con el anterior ejemplo:
    "({}{}{})" en count se agregan '(','{' cuando llega a '}' reconoce que es un caracter de close y usa la funcion
    open.index(count.pop()) donde count.pop() es igual al ultimo caracter de la lista count osea '{' y este devuelve el indice
    que coincide con el de close y elimina ambos de la lista osea "({}{}{})" --> "({}{})" --> "({})" --> "()" --> ""

    * .pop() elimina y retorna el ultimo valor de lista, mientras que .pop(0) elimina y retorna el primero
"""


a = is_paired("({}{}{})")
print(a)