import math

figure = input()
area = 0.0

if figure == "square":
    side = float(input())
    area = side ** 2
elif figure == "rectangle":
    sideA = float(input())
    sideB = float(input())
    area = sideA * sideB
elif figure == "circle":
    radius = float(input())
    area = math.pi * radius ** 2
elif figure == "triangle":
    side = float(input())
    height = float(input())
    area = side * height / 2

print(f"{area:.3f}")
