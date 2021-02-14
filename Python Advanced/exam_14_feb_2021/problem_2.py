from math import floor


def is_valid(n, pot_row, pot_col):
    return 0 <= pot_row < n and 0 <= pot_col < n


n = int(input())
matrix = []
player_position = []

for i in range(n):
    line = [char for char in input().split()]
    matrix.append(line)
    if "P" in line:
        player_column_index = line.index("P")
        player_row_index = i
        player_position = [player_row_index, player_column_index]

commands = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
is_out = False
total_coins = 0
path = []

while total_coins <= 100:
    command = input()
    start_row, start_column = player_position
    new_row, new_column = commands[command]
    potential_row = start_row + new_row
    potential_col = start_column + new_column

    if is_valid(n, potential_row, potential_col):
        if matrix[potential_row][potential_col].isdigit():
            number = int(matrix[potential_row][potential_col])
            total_coins += number
        elif matrix[potential_row][potential_col] == "X":
            total_coins = total_coins / 2
            is_out = True
            break
        player_position = [potential_row, potential_col]
        path.append(player_position)
    else:
        total_coins = total_coins / 2
        is_out = True
        break
    if total_coins >= 100:
        break

if is_out:
    print(f"Game over! You've collected {floor(total_coins)} coins.")
else:
    print(f"You won! You've collected {total_coins} coins.")

print("Your path:")
print(*[p for p in path], sep='\n')
