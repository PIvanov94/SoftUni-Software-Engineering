import math

hours_need = int(input())
days = int(input())
emp_cnt = int(input())

work_hours = days * 0.90 * 8
emp_overtime = emp_cnt * (2 * days)
total_time = math.floor(work_hours + emp_overtime)

if total_time >= hours_need:
    hours_left = total_time - hours_need
    print(f"Yes!{hours_left} hours left.")
else:
    hours_need_final = hours_need - total_time
    print(f"Not enough time!{hours_need_final} hours needed.")