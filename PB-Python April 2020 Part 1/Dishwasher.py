bottles = int(input())

detergent_quantity = bottles * 750
counter = 0
dishes = 0
pots = 0

while detergent_quantity >= 0:
    command = input()
    counter += 1
    if command == "End":
        break
    if counter % 3 != 0:
        detergent_quantity -= int(command) * 5
        dishes += int(command)
    else:
        detergent_quantity -= int(command) * 15
        pots += int(command)

if detergent_quantity >= 0:
    print("Detergent was enough!")
    print(f"{dishes} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {detergent_quantity} ml.")
else:
    print(f"Not enough detergent, {abs(detergent_quantity)} ml. more necessary!")