rows = int(input())
students = {}
average_grades = {}
for el in range(rows):
    student_name = input()
    grade = float(input())

    if student_name not in students:
        students[student_name] = []
    students[student_name].append(grade)

for student, grade in students.items():
    average_grade = sum(grade) / len(grade)
    if average_grade >= 4.5:
        average_grades[student] = average_grade

sorted_grades = sorted(average_grades.items(), key=lambda x: x[1], reverse=True)

for key, value in sorted_grades:
    print(f"{key} -> {value:.2f}")