import math

guests_cnt = int(input())
budget = int(input())

kozunak_cnt = math.ceil(guests_cnt / 3)
eggs_cnt = guests_cnt * 2

kozunak_price = kozunak_cnt * 4
eggs_price = eggs_cnt * 0.45
total_price = kozunak_price + eggs_price

if total_price <= budget:
    print(f"Lyubo bought {kozunak_cnt} Easter bread and {eggs_cnt} eggs.")
    print(f"He has {budget - total_price:.2f} lv. left.")
else:
    money_need = total_price - budget
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {money_need:.2f} lv. more.")