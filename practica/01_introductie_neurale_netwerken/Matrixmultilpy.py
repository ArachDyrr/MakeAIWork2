# my own matrix multiplication function

class Matrixmultiply:
    """A class to multiply matrixes."""

    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


    # create the function to multiply the 2 matrixes

    def matrix_multiply_result(self, matrix1, matrix2):
        # transpose matrix_2
        matrix2transposed = list(map(list, zip(*matrix2)))

        # create the new matrix for the multiplication result
        matrix3 = []

        # cycle true the matrixes to calculate the cells for m3 row by row and add them to the new matrix
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix2[0])):
                cel = list(map(lambda x, y: x * y, matrix1[i], matrix2transposed[j]))
                cel_s = sum(cel)
                row.append(cel_s)
            matrix3.append(row)

        return matrix3

