def spiral_matrix(size):
    value = 1
    matriz = [[0 for _ in range(size)] for _ in range(size)]

    left, right, top, bottom = 0, size - 1, 0, size - 1

    while left <= right and top <= bottom:

        for j in range(left, right + 1):
            matriz[top][j] = value
            value += 1
        top += 1


        for i in range(top, bottom + 1):
            matriz[i][right] = value
            value += 1
        right -= 1

        if top <= bottom:
            for j in range(right, left - 1, -1):
                matriz[bottom][j] = value
                value += 1
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                matriz[i][left] = value
                value += 1
            left += 1

    return matriz


a = spiral_matrix(3)
print(a)