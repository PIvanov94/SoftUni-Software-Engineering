budget = float(input())
gas_need = float(input())
day_of_week = str(input())

gas_price_for_liter = 2.10
guide_price = 100

gas_total_price = gas_need * gas_price_for_liter
total_price = gas_total_price + guide_price

if day_of_week == "Saturday":
    total_price *= 0.90
elif day_of_week == "Sunday":
    total_price *= 0.80
if budget >= total_price:
    money_left = budget - total_price
    print(f"Safari time! Money left: {money_left:.2f} lv. ")
elif total_price > budget:
    money_need = total_price - budget
    print(f"Not enough money! Money needed: {money_need:.2f} lv.")