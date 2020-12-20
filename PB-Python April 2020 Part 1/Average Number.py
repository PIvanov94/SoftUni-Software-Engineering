n = int(input())
average = 0

for i in range(1, n + 1):
    number = int(input())
    average += number / n

print(f"{average:.2f}")