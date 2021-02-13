def init_matrix():
    n = int(input())
    matrix = [[0 for x in range(n)] for _ in range(n)]
    return matrix


def plant_mines(bombs_count, matrix):
    for _ in range(bombs_count):
        row_index, column_index = [int(el) for el in input()[1:-1].split(", ")]
        matrix[row_index][column_index] = "*"

        if row_index - 1 in range(len(matrix)) and matrix[row_index - 1][column_index] != "*":  # up
            matrix[row_index - 1][column_index] += 1
        if row_index + 1 in range(len(matrix)) and matrix[row_index + 1][column_index] != "*":  # down
            matrix[row_index + 1][column_index] += 1
        if column_index - 1 in range(len(matrix)) and matrix[row_index][column_index - 1] != "*":  # left
            matrix[row_index][column_index - 1] += 1
        if column_index + 1 in range(len(matrix)) and matrix[row_index][column_index + 1] != "*":  # right
            matrix[row_index][column_index + 1] += 1

        if row_index - 1 in range(len(matrix)) and column_index - 1 in range(len(matrix)) and matrix[row_index - 1][
            column_index - 1] != "*":
            matrix[row_index - 1][column_index - 1] = int(
                matrix[row_index - 1][column_index - 1]) + 1  # up left diagonal

        if row_index - 1 in range(len(matrix)) and column_index + 1 in range(len(matrix)) and matrix[row_index - 1][
            column_index + 1] != "*":
            matrix[row_index - 1][column_index + 1] = int(
                matrix[row_index - 1][column_index + 1]) + 1  # up right diagonal

        if row_index + 1 in range(len(matrix)) and column_index - 1 in range(len(matrix)) and matrix[row_index + 1][
            column_index - 1] != "*":
            matrix[row_index + 1][column_index - 1] = int(
                matrix[row_index + 1][column_index - 1]) + 1  # down left diagonal

        if row_index + 1 in range(len(matrix)) and column_index + 1 in range(len(matrix)) and matrix[row_index + 1][
            column_index + 1] != "*":
            matrix[row_index + 1][column_index + 1] = int(
                matrix[row_index + 1][column_index + 1]) + 1  # down right diagonal

    matrix = [" ".join([str(el) for el in el]) for el in matrix]
    return matrix


matrix = init_matrix()
bombs_count = int(input())
matrix = plant_mines(bombs_count, matrix)

print(*[el for el in matrix], sep='\n')
