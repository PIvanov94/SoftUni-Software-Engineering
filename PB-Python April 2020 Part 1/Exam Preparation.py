failed_grades_cnt = int(input())
failed_times = 0
solved_problems_cnt = 0
grades_sum = 0
last_problem = ""
has_failed = True

while failed_times < failed_grades_cnt:
    problem_name = input()
    if problem_name == "Enough":
        has_failed = False
        break
    grade = int(input())
    if grade <= 4:
        failed_times += 1
    grades_sum += grade
    solved_problems_cnt += 1
    last_problem = problem_name

if has_failed:
    print(f"You need a break, {failed_grades_cnt} poor grades.")
else:
    print(f"Average score: {grades_sum / solved_problems_cnt:.2f}")
    print(f"Number of problems: {solved_problems_cnt}")
    print(f"Last problem: {last_problem}")