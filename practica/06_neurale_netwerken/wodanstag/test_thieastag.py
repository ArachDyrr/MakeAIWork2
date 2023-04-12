from HombrewMatrix import Matrix

list0 = [[1,2,3],[4,5,6]]
list1 = [[1,2],[3,4],[5,6]]

matrix0 = Matrix(list0)
matrix1 = Matrix(list1)

matrix0_shapecheck = matrix0.matrix_shape_check()
print(matrix0_shapecheck)

print(matrix0 == matrix1)

matrix_multiplied = matrix0 * matrix1

# matrix_multiplied = matrix_multiplied.printable()
print (matrix_multiplied)
