guests_cnt = int(input())
lunch_price = float(input())
budget_desi = float(input())

cake_price = budget_desi * 0.10

if 10 <= guests_cnt <= 15:
    lunch_price *= 0.85
elif 15 < guests_cnt <= 20:
    lunch_price *= 0.80
elif guests_cnt > 20:
    lunch_price *= 0.75

total_price = guests_cnt * lunch_price + cake_price

if budget_desi > total_price:
    money_left = budget_desi - total_price
    print(f"It is party time! {money_left:.2f} leva left.")
else:
    money_need = total_price - budget_desi
    print(f"No party! {money_need:.2f} leva needed.")
