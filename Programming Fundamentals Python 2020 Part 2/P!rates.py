data = input()

cities = {}

while not data == "Sail":
    city, population, gold = data.split("||")
    population = int(population)
    gold = int(gold)
    if city not in cities:
        cities[city] = {"population": population, "gold": gold}
    else:
        cities[city]["population"] += population
        cities[city]["gold"] += gold
    data = input()

line = input()

while not line == "End":
    data = line.split("=>")
    command = data[0]
    city = data[1]
    if command == "Plunder":
        people = int(data[2])
        gold = int(data[3])
        cities[city]["population"] -= people
        cities[city]["gold"] -= gold
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities[city]["population"] == 0 or cities[city]["gold"] == 0:
            del cities[city]
            print(f"{city} has been wiped off the map!")
    elif command == "Prosper":
        gold = int(data[2])
        if gold >= 0:
            cities[city]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")
        else:
            print("Gold added cannot be a negative number!")

    line = input()

sorted_towns = sorted(cities.items(), key=lambda x: (-x[1]['gold'], x[0]))
print(f"Ahoy, Captain! There are {len(sorted_towns)} wealthy settlements to go to:")
for town, value in sorted_towns:
    if sorted_towns:
        print(f"{town} -> Population: {value['population']} citizens, Gold: {value['gold']} kg")
    else:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")