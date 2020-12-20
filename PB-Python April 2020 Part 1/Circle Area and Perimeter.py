import math

r = float(input())

area_of_circle = math.pi * (math.pow(r, 2))
perimeter_of_circle = math.pi * (r * 2)

print(f"{area_of_circle:.2f}")
print(f"{perimeter_of_circle:.2f}")