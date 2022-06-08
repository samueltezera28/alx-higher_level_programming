def square_matrix_simple(matrix=[]):

    new_matrix = matrix
    for i in len(new_matrix):
        for j in len(new_matrix):
            new_matrix=row*row
    return new_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(square_matrix_simple(matrix))