mackerel_price_for_kg = float(input())
sprat_price_for_kg = float(input())
chamois_kg = float(input())
horse_mackerel_kg = float(input())
mussels_kg = int(input())

chamois_price_for_kg = mackerel_price_for_kg * 1.6
horse_mackerel_price_for_kg = sprat_price_for_kg * 1.8
mussels_price_for_kg = 7.5

sum_for_chamois = chamois_kg * chamois_price_for_kg
sum_for_horse_mackerel = horse_mackerel_kg * horse_mackerel_price_for_kg
sum_for_mussels = mussels_kg * mussels_price_for_kg

total = sum_for_chamois + sum_for_horse_mackerel + sum_for_mussels

print(f"{total:.2f}")
