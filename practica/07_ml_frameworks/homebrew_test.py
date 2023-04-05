import homebrew_functions as hb

matrix_1 =[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
matrix_2 = [[1,2,3,4,5,6],[5,6,7,8,5,6],[9,10,11,12,5,6]]

# matrix_1 =[[-1,-1]]
# matrix_2 = [[1],[1]]
# print (matrix_1)
result = hb.matrix_multiplication(matrix_1,matrix_2)

print (result)

check = hb.matrix_shape_check(matrix_1)

print (check)
print('# -------------------------------')

circle = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
    ]

matrix = circle

I_n = hb.initial_input(matrix)
W_n = hb.initial_random_weights(matrix)

print (I_n)
print()
print(W_n)

matrix_1=I_n
matrix_2= W_n
result = hb.matrix_multiplication(matrix_2,matrix_1)

print (result)

check = hb.matrix_shape_check(matrix_1)

print (check)