energy = int(input())

command = input()
won_battles = 0

while not command == "End of battle":
    distance = int(command)
    if energy >= distance:
        won_battles += 1
        energy -= distance
        if won_battles % 3 == 0:
            energy += won_battles
    else:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
        break

    command = input()

else:
    print(f"Won battles: {won_battles}. Energy left: {energy}")