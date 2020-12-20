budget = int(input())
season = input()
fishermen_cnt = int(input())

rent_ship = 0

if season == "Spring":
    rent_ship = 3000
elif season == "Summer" or season == "Autumn":
    rent_ship = 4200
elif season == "Winter":
    rent_ship = 2600
if fishermen_cnt <= 6:
    rent_ship *= 0.90
elif 7 <= fishermen_cnt <= 11:
    rent_ship *= 0.85
elif fishermen_cnt >= 12:
    rent_ship *= 0.75
if fishermen_cnt % 2 == 0 and not season == "Autumn":
    rent_ship *= 0.95
if budget >= rent_ship:
    money_left = budget - rent_ship
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    money_need = rent_ship - budget
    print(f"Not enough money! You need {money_need:.2f} leva.")
