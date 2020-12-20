flour_price_per_kg = float(input())
flour_kg = float(input())
sugar_kg = float(input())
eggs_packs = int(input())
yeast_packs = int(input())

sugar_price_per_kg = flour_price_per_kg * 0.75
eggs_price_per_pack = flour_price_per_kg * 1.10
yeast_price_per_pack = sugar_price_per_kg * 0.20

flour_total_price = flour_price_per_kg * flour_kg
sugar_total_price = sugar_price_per_kg * sugar_kg
eggs_total_price = eggs_price_per_pack * eggs_packs
yeast_total_price = yeast_price_per_pack * yeast_packs

total_price = flour_total_price + sugar_total_price + eggs_total_price + yeast_total_price

print(f"{total_price:.2f}")