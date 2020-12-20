data = input()
courses = {}
regs_for_course = {}

while not data == "end":
    course_name, student_name = data.split(" : ")
    if course_name not in courses:
        courses[course_name] = [student_name]
        regs_for_course[course_name] = 1
    else:
        courses[course_name].append(student_name)
        regs_for_course[course_name] += 1
    data = input()

regs_for_course = dict(sorted(regs_for_course.items(), key=lambda x: (-x[1])))

for key, value in regs_for_course.items():
    print(f"{key}: {value}")
    for val in sorted(courses[key]):
        print(f"-- {val}")