factor = int(input())
count = int(input())
elements = []

for num in range(1, count + 1):
    number = num * factor
    if number % factor == 0:
        elements.append(number)

print(elements)