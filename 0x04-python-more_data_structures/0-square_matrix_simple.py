def square_matrix_simple(matrix=[]):

    new_matrix = [[x ** 2 for x in row] for row in matrix]
    return new_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(square_matrix_simple(matrix))