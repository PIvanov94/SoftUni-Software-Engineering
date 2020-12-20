import math

days_off = int(input())
animals_food_kg = int(input())
daily_dog_food_kg = float(input())
daily_cat_food_kg = float(input())
daily_turtle_food_g = float(input())

dog_food_sum = days_off * daily_dog_food_kg
cat_food_sum = days_off * daily_cat_food_kg
turtle_food_sum = (days_off * daily_turtle_food_g) / 1000
total_food_sum = dog_food_sum + cat_food_sum + turtle_food_sum

if animals_food_kg >= total_food_sum:
    food_left = animals_food_kg - total_food_sum
    print(f"{math.floor(food_left)} kilos of food left.")
else:
    food_need = total_food_sum - animals_food_kg
    print(f"{math.ceil(food_need)} more kilos of food are needed.")