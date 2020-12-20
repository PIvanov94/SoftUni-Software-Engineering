quantity = int(input())
days = int(input())

ornament_set_price = 2
tree_skirt_price = 5
tree_garlands_price = 3
tree_lights_price = 15

christmas_spirit = 0
total_cost = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total_cost += ornament_set_price * quantity
        christmas_spirit += 5
    if day % 3 == 0:
        total_cost += (tree_skirt_price * quantity) + (tree_garlands_price * quantity)
        christmas_spirit += 13
    if day % 5 == 0:
        total_cost += tree_lights_price * quantity
        christmas_spirit += 17
        if day % 3 == 0:
            christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        total_cost += tree_lights_price + tree_garlands_price + tree_skirt_price
        if day == days:
            christmas_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {christmas_spirit}")
