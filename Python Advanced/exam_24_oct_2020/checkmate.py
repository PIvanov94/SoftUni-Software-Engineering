board = []
queens = []
king_row_index = ""
king_column_index = ""
n = 8

for i in range(n):
    line = [char for char in input().split()]
    board.append(line)
    if "K" in line:
        king_column_index = line.index("K")  # king mark
        king_row_index = i

rows_count = len(board)
columns_count = len(board[0])

for column_index in range(king_column_index + 1, columns_count):
    # right
    if board[king_row_index][column_index] == "Q":  # queen mark
        queens.append([king_row_index, column_index])
        break

for column_index in range(king_column_index - 1, -1, -1):
    # left
    if board[king_row_index][column_index] == "Q":
        queens.append([king_row_index, column_index])
        break

for row_index in range(king_row_index - 1, -1, -1):
    # up
    if board[row_index][king_column_index] == "Q":
        queens.append([row_index, king_column_index])
        break

for row_index in range(king_row_index + 1, rows_count):
    # down
    if board[row_index][king_column_index] == "Q":
        queens.append([row_index, king_column_index])
        break

for right_down_diagonal in range(len(board)):
    if board[king_row_index+1][king_column_index+1] == "Q":
        queens.append([king_row_index+1, king_column_index+1])
        break

for left_down_diagonal in range(len(board) - 1, -1, -1):
    if board[king_row_index+1][king_column_index-1] == "Q":
        queens.append([king_row_index+1, king_column_index-1])
        break

for right_up_diagonal in range(len(board)):
    if board[king_row_index-1][king_column_index+1] == "Q":
        queens.append([king_row_index-1, king_column_index+1])
        break

for left_up_diagonal in range(len(board) -1, -1, -1):
    if board[king_row_index-1][king_column_index-1] == "Q":
        queens.append([king_row_index-1, king_column_index-1])
        break

if queens:
    for queen in queens:
        print(queen)
else:
    print("The king is safe!")
