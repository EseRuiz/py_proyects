def rows(row_count):
    if row_count < 0:
        raise ValueError("number of rows is negative")
    if row_count == 0:
        return []
    if row_count == 1:
        return [[1]]
    
    fil_anterior = rows(row_count-1)
    fil_actual = [1]

    for i in range(len(fil_anterior[-1]) - 1):
        fil_actual.append(fil_anterior[-1][i] + fil_anterior[-1][i + 1])

    fil_actual.append(1)

    res = fil_anterior
    res.append(fil_actual)

    return res

a = rows(3)
print(a)
TRIANGLE = [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1],
]
print(TRIANGLE[:3])

# Ejemplo de Ejecución
# Supongamos que llamamos a rows(3):

# rows(3) llama a rows(2).
# rows(2) llama a rows(1).
# rows(1) retorna [[1]].
# rows(2) recibe [[1]] y construye:
# fil_anterior es [[1]]
# fil_actual es [1, 1]
# Retorna [[1], [1, 1]]
# rows(3) recibe [[1], [1, 1]] y construye:
# fil_anterior es [[1], [1, 1]]
# fil_actual es [1, 2, 1] (calculado sumando 1+1 del paso anterior)
# Retorna [[1], [1, 1], [1, 2, 1]]
# Así, la función construye el Triángulo de Pascal recursivamente fila por fila.