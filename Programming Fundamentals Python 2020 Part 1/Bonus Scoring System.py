students_cnt = int(input())
lectures_cnt = int(input())
initial_bonus = int(input())
max_bonus = 0
max_student_attendance = 0

for student in range(1, students_cnt + 1):

    student_attendance = int(input())
    total_bonus = student_attendance / lectures_cnt * (5 + initial_bonus)
    if total_bonus >= max_bonus:
        max_bonus = total_bonus
    if student_attendance >= max_student_attendance:
        max_student_attendance = student_attendance

print(f"Max Bonus: {round(max_bonus)}.")
print(f"The student has attended {max_student_attendance} lectures.")