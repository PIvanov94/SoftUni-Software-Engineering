name = input()
grades = 1
sum_grades = 0
regrades = 0

while grades <= 12:
    evaluation = float(input())
    if evaluation < 4:
        regrades += 1
        if regrades == 2:
            break

        continue
    sum_grades += evaluation
    grades += 1

if grades == 13:
    average = sum_grades / 12
    print(f"{name} graduated. Average grade: {average:.2f}")
else:
    print(f"{name} has been excluded at {grades} grade")