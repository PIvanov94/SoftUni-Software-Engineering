judges_cnt = int(input())
project_name = input()
total_sum = 0
count_grades = 0

while project_name != "Finish":
    sum_grades = 0
    for judge in range(1, judges_cnt + 1):
        grades = float(input())
        sum_grades += grades
        count_grades += 1
    average = sum_grades / judges_cnt
    total_sum += sum_grades

    print(f"{project_name} - {average:.2f}.")
    project_name = input()

print(f"Student's final assessment is {(total_sum / count_grades):.2f}.")