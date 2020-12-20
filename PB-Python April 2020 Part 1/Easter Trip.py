destination = input()
booking_dates = input()
nights_cnt = int(input())
total_price = 0
night_price = 0

if destination == "France":
    if booking_dates == "21-23":
        night_price = 30
    elif booking_dates == "24-27":
        night_price = 35
    elif booking_dates == "28-31":
        night_price = 40
elif destination == "Italy":
    if booking_dates == "21-23":
        night_price = 28
    elif booking_dates == "24-27":
        night_price = 32
    elif booking_dates == "28-31":
        night_price = 39
elif destination == "Germany":
    if booking_dates == "21-23":
        night_price = 32
    elif booking_dates == "24-27":
        night_price = 37
    elif booking_dates == "28-31":
        night_price = 43

total_price = nights_cnt * night_price

print(f"Easter trip to {destination} : {total_price:.2f} leva.")