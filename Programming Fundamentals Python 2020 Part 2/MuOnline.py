rooms = input().split("|")
initial_health = 100
initial_bitcoins = 0
room_counter = 0

for room in rooms:
    command, number = room.split(" ")
    if command == "potion":
        initial_health += int(number)
        if initial_health > 100:
            healed_hp = 100 - (initial_health - int(number))
            initial_health = 100
            print(f"You healed for {healed_hp} hp.")
            print(f"Current health: {initial_health} hp.")
        else:
            print(f"You healed for {number} hp.")
            print(f"Current health: {initial_health} hp.")
        room_counter += 1
    elif command == "chest":
        initial_bitcoins += int(number)
        print(f"You found {number} bitcoins.")
        room_counter += 1
    else:
        initial_health -= int(number)
        if initial_health > 0:
            print(f"You slayed {command}.")
            room_counter += 1
        else:
            room_counter += 1
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_counter}")
            break

if initial_health > 0:
    print(f'You\'ve made it!\nBitcoins: {initial_bitcoins}\nHealth: {initial_health}')
