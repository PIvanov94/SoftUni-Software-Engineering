import math

magnolias_cnt = int(input())
hyacinths_cnt = int(input())
roses_cnt = int(input())
cactus_cnt = int(input())
present_price = float(input())

magnolias_price = magnolias_cnt * 3.25
hyacinths_price = hyacinths_cnt * 4
roses_price = roses_cnt * 3.50
cactus_price = cactus_cnt * 8
total_price_with_tax = (magnolias_price + hyacinths_price + roses_price + cactus_price) * 0.95

if total_price_with_tax >= present_price:
    money_left = total_price_with_tax - present_price
    print(f"She is left with {math.floor(money_left)} leva.")
else:
    money_need = present_price - total_price_with_tax
    print(f"She will have to borrow {math.ceil(money_need)} leva.")