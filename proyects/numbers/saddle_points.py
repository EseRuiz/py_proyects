def saddle_points(matrix):
    for i in range(len(matrix)-1):
        if len(matrix[i]) != len(matrix[i+1]):
            raise ValueError("irregular matrix")

    max_val = [max(row) for row in (matrix)]
    columns = [val for val in zip(*matrix)]
    res = []
    for i in range(len(max_val)):
        for j in range(len(columns)):
            if max_val[i] == min(columns[j]):
                res.append({"row": i+1, "column": j+1})
    return res

# matrix = [[9, 8, 7], [5, 3, 2], [6, 6, 7]]
# a = saddle_points(matrix)
# print(a)
