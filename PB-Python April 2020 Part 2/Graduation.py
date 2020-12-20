name = input()
grades = 1
sum_grades = 0

while grades <= 12:
    evaluation = float(input())
    if evaluation < 4:
        continue
    sum_grades += evaluation
    grades += 1

average = sum_grades / 12

print(f"{name} graduated. Average grade: {average:.2f}")
