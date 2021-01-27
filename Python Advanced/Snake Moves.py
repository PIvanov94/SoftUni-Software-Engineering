from collections import deque

rows, cols = [int(el) for el in input().split()]
snake = deque(list(input()))

for row in range(rows):
    snakes_path = ""
    for col in range(cols):
        snakes_piece = snake.popleft()
        snakes_path += snakes_piece
        snake.append(snakes_piece)
    if row % 2 == 0:
        print(snakes_path)
    else:
        print(snakes_path[::-1])