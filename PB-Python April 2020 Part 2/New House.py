flower_type = input()
cnt_flowers = int(input())
budget = int(input())

total_price = 0

if flower_type == "Roses":
    total_price = cnt_flowers * 5
    if cnt_flowers > 80:
        total_price *= 0.9
elif flower_type == "Dahlias":
    total_price = cnt_flowers * 3.8
    if cnt_flowers > 90:
        total_price *= 0.85
elif flower_type == "Tulips":
    total_price = cnt_flowers * 2.8
    if cnt_flowers > 80:
        total_price *= 0.85
elif flower_type == "Narcissus":
    total_price = cnt_flowers * 3
    if cnt_flowers < 120:
        total_price *= 1.15
elif flower_type == "Gladiolus":
    total_price = cnt_flowers * 2.5
    if cnt_flowers < 80:
        total_price *= 1.2

if budget >= total_price:
    money_left = budget - total_price
    print(f"Hey, you have a great garden with {cnt_flowers} {flower_type} and {money_left:.2f} leva left.")
else:
    money_need = total_price - budget
    print(f"Not enough money, you need {money_need:.2f} leva more.")