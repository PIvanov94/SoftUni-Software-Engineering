n = int(input())
result = 0
line_one = 0
line_two = 0
line_three = 0
line_four = 0
line_five = 0
invalid_line = 0

for i in range(1, n + 1):
    number = int(input())
    if 0 <= number <= 9:
        result += number * 0.2
        line_one += 1
    elif 10 <= number <= 19:
        result += number * 0.3
        line_two += 1
    elif 20 <= number <= 29:
        result += number * 0.4
        line_three += 1
    elif 30 <= number <= 39:
        result += 50
        line_four += 1
    elif 40 <= number <= 50:
        result += 100
        line_five += 1
    else:
        result /= 2
        invalid_line += 1

line_one_percentages = line_one / n * 100
line_two_percentages = line_two / n * 100
line_three_percentages = line_three / n * 100
line_four_percentages = line_four / n * 100
line_five_percentages = line_five / n * 100
invalid_percentages = invalid_line / n * 100

print(f"{result:.2f}")
print(f"From 0 to 9: {line_one_percentages:.2f}%")
print(f"From 10 to 19: {line_two_percentages:.2f}%")
print(f"From 20 to 29: {line_three_percentages:.2f}%")
print(f"From 30 to 39: {line_four_percentages:.2f}%")
print(f"From 40 to 50: {line_five_percentages:.2f}%")
print(f"Invalid numbers: {invalid_percentages:.2f}%")