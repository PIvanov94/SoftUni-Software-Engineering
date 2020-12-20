km_cnt = int(input())
travel_time = input()

taxi_price_day = km_cnt * 0.79 + 0.70
taxi_price_night = km_cnt * 0.90 + 0.70
bus_price = km_cnt * 0.09
train_price = km_cnt * 0.06

if km_cnt < 20 and travel_time == "day":
    print(f"{taxi_price_day:.2f}")
elif km_cnt < 20 and travel_time == "night":
    print(f"{taxi_price_night:.2f}")
elif 20 <= km_cnt < 100:
    print(f"{bus_price:.2f}")
elif km_cnt >= 100:
    print(f"{train_price:.2f}")