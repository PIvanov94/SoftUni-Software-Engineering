cargo_cnt = int(input())

cargo_all = 0
cargo_price = 0
bus_sum = 0
truck_sum = 0
train_sum = 0

for i in range(1, cargo_cnt + 1):
    tons_cargo = int(input())
    cargo_all += tons_cargo
    if tons_cargo <= 3:
        cargo_price = 200
        bus_sum += cargo_price * tons_cargo
    elif 4 <= tons_cargo <= 11:
        cargo_price = 175
        truck_sum += cargo_price * tons_cargo
    elif tons_cargo >= 12:
        cargo_price = 120
        train_sum += cargo_price * tons_cargo

average = (bus_sum + truck_sum + train_sum) / cargo_all
bus_percentages = (bus_sum / 200) / cargo_all * 100
truck_percentages = (truck_sum / 175) / cargo_all * 100
train_percentages = (train_sum / 120) / cargo_all * 100

print(f"{average:.2f}")
print(f"{bus_percentages:.2f}%")
print(f"{truck_percentages:.2f}%")
print(f"{train_percentages:.2f}%")
