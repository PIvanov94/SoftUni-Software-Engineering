initial_string = input()
n = int(input())

matrix = []
row_index = ""
col_index = ""

for i in range(n):
    line = [char for char in input()]
    matrix.append(line)
    if "P" in line:
        col_index = line.index("P")
        row_index = i

number_movements = int(input())

for _ in range(number_movements):
    command = input()
    matrix[row_index][col_index] = "-"
    if command == "up" and row_index > 0:
        row_index -= 1
    elif command == "down" and row_index < n - 1:
        row_index += 1
    elif command == "left" and col_index > 0:
        col_index -= 1
    elif command == "right" and col_index < n - 1:
        col_index += 1
    else:
        initial_string = initial_string[:-1]

    if matrix[row_index][col_index].isalpha():
        initial_string += matrix[row_index][col_index]
    matrix[row_index][col_index] = "P"

print(initial_string)

for row in matrix:
    print("".join(row))