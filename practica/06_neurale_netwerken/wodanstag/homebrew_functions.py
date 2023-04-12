import random

# create the check to see if the matrix has the same amount of items per row


def matrix_shape_check(matrix):
    """Checks if all rows in a matrix have the same amount of items"""
    row_nr = 0
    base_row_length = len(matrix[0])
    for item in matrix:
        rows_col = len(matrix[row_nr])
        if base_row_length != rows_col:
            print(f'Error in {matrix} {item}')
            return False
        row_nr += 1
    return True


# create the function to multiply the 2 matrixes

def matrix_multiplication(matrix1, matrix2):
    """multiplies two matrixes if permitted"""
    # check if both lists of lists have the proper shape to be a matrix.

    if len(matrix1[0]) == len(matrix2):
        pass
    # DeMorgan
    # not (A and B) == not A or not B

        if not (matrix_shape_check(matrix1) and matrix_shape_check(matrix2)):
            return None
    else:
        print('Matrix shapes != match!')
        return None

    # transpose matrix_2
    matrix2t = list(map(list, zip(*matrix2)))

    # create the new matrix for the multiplication result
    matrix3 = []

    # cycle true the matrixes to calculate the cells for matrix3 row by row and add them to the new matrix
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            cel = list(map(lambda x, y: x * y, matrix1[i], matrix2t[j]))
            cel_s = sum(cel)
            row.append(cel_s)
        matrix3.append(row)

    return matrix3


def initial_input(list_of_list_matrix):
    """flaten a matrix to ( n * 0) """
    flattned_matrix = [sum(list_of_list_matrix, [])]
    initial_matrix = list(map(list, zip(*flattned_matrix)))
    return initial_matrix
    # return flattned_matrix


# a function to generate random weights
def initial_random_weights(i_n):
    """generate random weights totaling to 1"""

    i_n = [sum(i_n, [])]

    # Generate n random values
    initial_weights = [random.random() for i in range(len(i_n[0]))]

    # Calculate the sum of the random values
    weight_sum = sum(initial_weights)

    # Divide each random value by the sum to normalize them
    random_weights = [round(item/weight_sum,2) for item in initial_weights]

    return [random_weights]
