budget = float(input())
kg_flour_price = float(input())

eggs_pack_price = kg_flour_price * 0.75
liter_milk_price = kg_flour_price * 1.25

cozonac_price = kg_flour_price + eggs_pack_price + (liter_milk_price * 0.250)
cozonacs_made = 0
colored_eggs = 0

while budget > cozonac_price:
    cozonacs_made += 1
    colored_eggs += 3
    if cozonacs_made % 3 == 0:
        colored_eggs -= cozonacs_made - 2

    budget -= cozonac_price

print(f"You made {cozonacs_made} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")