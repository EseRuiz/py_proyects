class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string.split("\n")
        

    def row(self, index):
        res = self.matrix_string[index-1].split()
        res_int = [int(val) for val in res]
        return res_int

    def column(self, index):
        data = self.matrix_string
        split_data = [i.split() for i in data]
        columns = [val for val in zip(*split_data)]
        res = list(columns[index-1])
        res_int = [int(val) for val in res]
        return res_int

matrix = Matrix("1 2 3\n4 5 6\n7 8 9")
print(matrix.column(3), [3, 6, 9])