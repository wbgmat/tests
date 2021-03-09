matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


def matriks():
    new_matrix = []
    for col in range(0, 3):
        for row in range(0, 3):
            new_matrix += [matrix[row][col]]
    return new_matrix


def list_comp():
    return [[matrix[row][col] for row in range(0, 3)] for col in range(0, 3)]


def macierz():
    for row in matrix:
        return row


print(macierz())
#print(matrix[1])