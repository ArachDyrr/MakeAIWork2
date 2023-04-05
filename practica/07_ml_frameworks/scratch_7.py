class Matrix:
    # create the check to see if the matrix has the same amount of items per row
    def __init__(self, argInput):
        self.input = argInput

    def matrix_multiplication(self, other_matrix):
        """multiplies two matrices if permitted"""
        # check if both matrices have the proper shape to be multiplied

        if len(self.input[0]) == len(other_matrix.input):
            pass
            # DeMorgan
            # not (A and B) == not A or not B

            if not (self.matrix_shape_check() and other_matrix.matrix_shape_check()):
                return None
        else:
            print('Matrix shapes do not match!')
            return None

        # transpose the second matrix
        other_matrix_t = list(map(list, zip(*other_matrix.input)))

        # create the new matrix for the multiplication result
        result_matrix = []

        # cycle through the matrices to calculate the cells for result_matrix row by row and add them to the new matrix
        for i in range(len(self.input)):
            row = []
            for j in range(len(other_matrix.input[0])):
                cell = list(map(lambda x, y: x * y, self.input[i], other_matrix_t[j]))
                cell_sum = sum(cell)
                row.append(cell_sum)
            result_matrix.append(row)

        return result_matrix

    def matrix_shape_check(self):
        """check if all rows in matrix have the same length"""
        shape = len(self.input[0])
        return all(len(row) == shape for row in self.input)

    matrix1 = Matrix([[1, 2, 3], [4, 5, 6]])
    matrix2 = Matrix([[7, 8], [9, 10], [11, 12]])

    result = matrix1.matrix_multiplication(matrix2)