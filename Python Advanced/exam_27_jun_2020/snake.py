def is_valid(n, pot_row, pot_col):
    return 0 <= pot_row < n and 0 <= pot_col < n


def get_matrix_positions(n, matrix):
    snake_position = []
    burrows = []
    for i in range(n):
        row = input()
        for j in range(n):
            if not row[j] == "-":
                matrix[i][j] = row[j]
                if row[j] == "S":
                    snake_position = [i, j]
                elif row[j] == "B":
                    burrows.append([i, j])
    return matrix, snake_position, burrows


n = int(input())
matrix = [n * ["-"] for m in range(n)]

matrix, start_position, burrows = get_matrix_positions(n, matrix)
commands = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
is_out = False
food_eaten = 0

while food_eaten < 10:
    command = input()
    start_row, start_column = start_position
    new_row, new_column = commands[command]
    potential_row = start_row + new_row
    potential_col = start_column + new_column

    if is_valid(n, potential_row, potential_col):
        if matrix[potential_row][potential_col] == "*":
            food_eaten += 1
        elif matrix[potential_row][potential_col] == "B":
            burrows.pop(burrows.index([potential_row, potential_col]))
            matrix[start_row][start_column] = "."
            matrix[potential_row][potential_col] = "."
            start_position = burrows[0]
            matrix[burrows[0][0]][burrows[0][1]] = "S"
            continue
        matrix[start_row][start_column] = "."
        matrix[potential_row][potential_col] = "S"
        start_position = [potential_row, potential_col]
    else:
        matrix[start_row][start_column] = "."
        is_out = True
        break

if is_out:
    print("Game over!")
else:
    print("You won! You fed the snake.")

print(f"Food eaten: {food_eaten}")
print(*[''.join(m) for m in matrix], sep='\n')