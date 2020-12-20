n = int(input())
plants = {}

for _ in range(n):
    plant, rarity = input().split("<->")
    plants[plant] = {"rarity": int(rarity), "rating": []}
data = input()

while not data == "Exhibition":
    command, line = data.split(": ")
    try:
        if command == "Rate":
            plant, rating = line.split(" - ")
            plants[plant]["rating"].append(int(rating))
        elif command == "Update":
            plant, new_rarity = line.split(" - ")
            plants[plant]["rarity"] = int(new_rarity)
        elif command == "Reset":
            plant = line
            plants[plant]["rating"].clear()
    except:
        print("error")
    data = input()

for plant_name, plant_data in plants.items():
    if plants[plant_name]['rating']:
        plants[plant_name]['average_r'] = sum(plants[plant_name]['rating']) / len(plants[plant_name]['rating'])
    else:
        plants[plant_name]['average_r'] = 0

sorted_plants = sorted(plants.items(), key=lambda x: (x[1]['rarity'], x[1]['average_r']), reverse=True)

print("Plants for the exhibition:")
for plant_name, value in sorted_plants:
    print(f"- {plant_name}; Rarity: {value['rarity']}; Rating: {value['average_r']:.2f}")
