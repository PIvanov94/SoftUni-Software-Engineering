travel_price = float(input())
puzzles_cnt = int(input())
talking_dolls_cnt = int(input())
teddy_bears_cnt = int(input())
minions_cnt = int(input())
trucks_cnt = int(input())

puzzles_price = puzzles_cnt * 2.60
talking_dolls_price = talking_dolls_cnt * 3
teddy_bears_price = teddy_bears_cnt * 4.10
minions_price = minions_cnt * 8.20
trucks_price = trucks_cnt * 2

total_price = puzzles_price + talking_dolls_price + teddy_bears_price + minions_price + trucks_price
total_cnt = puzzles_cnt + talking_dolls_cnt + teddy_bears_cnt + minions_cnt + trucks_cnt

if total_cnt >= 50:
    total_price = total_price * 0.75
total_price = total_price * 0.9 # след наем
if total_price >= travel_price:
    money_left = total_price - travel_price
    print(f"Yes! {money_left:.2f} lv left.")
elif total_price < travel_price:
    money_need = travel_price - total_price
    print(f"Not enough money! {money_need:.2f} lv needed.")