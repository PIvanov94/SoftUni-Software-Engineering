n = int(input())

p1 = 0
p2 = 0
p3 = 0

for number in range(1, n + 1):
    value = int(input())
    if value % 2 == 0:
        p1 += 1
    if value % 3 == 0:
        p2 += 1
    if value % 4 == 0:
        p3 += 1
percentages_p1 = p1 / n * 100
percentages_p2 = p2 / n * 100
percentages_p3 = p3 / n * 100

print(f"{percentages_p1:.2f}%")
print(f"{percentages_p2:.2f}%")
print(f"{percentages_p3:.2f}%")

