heroes = {h: {} for h in input().split(", ")}

command = input()

while not command == "End":
    name, item, price = command.split("-")
    price = int(price)
    if not heroes[name].get(item):
        heroes[name].update({item: price})
    command = input()

print(*[f"{key} -> Items: {len(value)}, Cost: {sum([value[price] for price in value])}" for key, value in heroes.items()], sep="\n")