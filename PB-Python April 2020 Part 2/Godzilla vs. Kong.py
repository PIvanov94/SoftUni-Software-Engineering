budget = float(input())
walk_ons = int(input())
clothing_price = float(input())

total_clothing_price = walk_ons * clothing_price

if walk_ons > 150:
    total_clothing_price *= 0.9
decor_money = budget *0.1
total_price_movie = decor_money + total_clothing_price

if total_price_movie <= budget:
    print("Action!")
    money_left = budget - total_price_movie
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
else:
    print("Not enough money!")
    money_need = total_price_movie - budget
    print(f"Wingard needs {money_need:.2f} leva more.")