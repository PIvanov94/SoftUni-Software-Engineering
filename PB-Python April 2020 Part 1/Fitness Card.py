available_price = float(input())
sex = input()
age = int(input())
sport = input()

sport_price = 0

if sport == "Gym":
    if sex == "m":
        sport_price = 42
    elif sex == "f":
        sport_price = 35
elif sport == "Boxing":
    if sex == "m":
        sport_price = 41
    elif sex == "f":
        sport_price = 37
elif sport == "Yoga":
    if sex == "m":
        sport_price = 45
    elif sex == "f":
        sport_price = 42
elif sport == "Zumba":
    if sex == "m":
        sport_price = 34
    elif sex == "f":
        sport_price = 31
elif sport == "Dances":
    if sex == "m":
        sport_price = 51
    elif sex == "f":
        sport_price = 53
elif sport == "Pilates":
    if sex == "m":
        sport_price = 39
    elif sex == "f":
        sport_price = 37

if age <= 19:
    sport_price *= 0.80

if sport_price <= available_price:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    need_money = sport_price - available_price
    print(f"You don't have enough money! You need ${need_money:.2f} more.")