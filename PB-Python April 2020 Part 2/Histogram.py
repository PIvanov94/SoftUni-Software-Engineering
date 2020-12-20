n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for number in range(1, n + 1):
    value = int(input())
    if value < 200:
        p1 += 1
    elif 200 <= value <= 399:
        p2 += 1
    elif 400 <= value <= 599:
        p3 += 1
    elif 600 <= value <= 799:
        p4 += 1
    elif value >= 800:
        p5 += 1

percentages_p1 = p1 / n * 100
percentages_p2 = p2 / n * 100
percentages_p3 = p3 / n * 100
percentages_p4 = p4 / n * 100
percentages_p5 = p5 / n * 100

print(f"{percentages_p1:.2f}%")
print(f"{percentages_p2:.2f}%")
print(f"{percentages_p3:.2f}%")
print(f"{percentages_p4:.2f}%")
print(f"{percentages_p5:.2f}%")
