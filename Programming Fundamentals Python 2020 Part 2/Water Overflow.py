n = int(input())
capacity = 255
sum_water = 0

for i in range(1, n + 1):
    water_quantity = int(input())
    if water_quantity + sum_water > capacity:
        print("Insufficient capacity!")
    else:
        sum_water += water_quantity
print(sum_water)