budget = float(input())
season = input()

total_price = 0
place = ""
holiday = ""

if season == "summer":
    if budget <= 100:
        total_price = budget * 0.70
        place = "Bulgaria"
        holiday = "Camp"
    elif budget <= 1000:
        total_price = budget * 0.60
        place = "Balkans"
        holiday = "Camp"
    else:
        total_price = budget * 0.10
        place = "Europe"
        holiday = "Hotel"
elif season == "winter":
    if budget <= 100:
        total_price = budget * 0.30
        place = "Bulgaria"
        holiday = "Hotel"
    elif budget <= 1000:
        total_price = budget * 0.20
        place = "Balkans"
        holiday = "Hotel"
    else:
        total_price = budget * 0.10
        place = "Europe"
        holiday = "Hotel"

money_spent = budget - total_price

print(f"Somewhere in {place}")
print(f"{holiday} - {money_spent:.2f}")
