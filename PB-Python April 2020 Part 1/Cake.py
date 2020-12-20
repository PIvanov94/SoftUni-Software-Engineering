width_cake = int(input())
length_cake = int(input())
pieces = width_cake * length_cake

while pieces > 0:
    command = input()
    if command == "STOP":
        print(f"{pieces} pieces are left.")
        break
    else:
        taken_pieces = int(command)
        pieces -= taken_pieces
else:
    print(f"No more cake left! You need {abs(pieces)} pieces more.")
