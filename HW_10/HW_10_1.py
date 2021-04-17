matrix_1 = [[11, 25, 17, 80], [42, 60, 11, 100], [18, 32, 38, 80], [56, 91, 71, 98]]
matrix_2 = [[80, 49, 10, 61], [49, 100, 73, 18], [31, 82, 46, 55], [18, 74, 66, 10]]


class Matrix:
    def __init__(self, nested_dict):
        self.nd = nested_dict
        self.matrix_finally = ""
        for row in self.nd:
            for el in row:
                self.matrix_finally += f" {el} "
            self.matrix_finally += f"\n"

    def __add__(self, other):
        self.nd_sum = [[self.nd[i][j] + other.nd[i][j] for j in range(len(self.nd[0]))]
                       for i in range(len(self.nd))]
        return Matrix(self.nd_sum)

    def __str__(self):
        return self.matrix_finally


m_1 = Matrix(matrix_1)
m_2 = Matrix(matrix_2)
print(m_1 + m_2)
