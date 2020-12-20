students_cnt = int(input())

average = 0
top_students = 0
very_good_students = 0
good_students = 0
failed_students = 0

for i in range(1, students_cnt + 1):
    grades = float(input())
    average += grades
    if grades < 3:
        failed_students += 1
    elif 3 <= grades <= 3.99:
        good_students += 1
    elif 4 <= grades <= 4.99:
        very_good_students += 1
    elif grades >= 5:
        top_students += 1

top_students_percentages = top_students / students_cnt * 100
very_good_students_percentages = very_good_students / students_cnt * 100
good_students_percentages = good_students / students_cnt * 100
failed_students_percentages = failed_students / students_cnt * 100
average_grade = average / students_cnt

print(f"Top students: {top_students_percentages:.2f}%")
print(f"Between 4.00 and 4.99: {very_good_students_percentages:.2f}%")
print(f"Between 3.00 and 3.99: {good_students_percentages:.2f}%")
print(f"Fail: {failed_students_percentages:.2f}%")
print(f"Average: {average_grade:.2f}")