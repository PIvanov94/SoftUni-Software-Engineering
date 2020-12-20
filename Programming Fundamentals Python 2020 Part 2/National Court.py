employee_one_efficiency = int(input())
employee_two_efficiency = int(input())
employee_three_efficiency = int(input())
people_count = int(input())

answered_people_per_hour = employee_one_efficiency + employee_two_efficiency + employee_three_efficiency
hour = 0

while people_count > 0:
    hour += 1
    people_count -= answered_people_per_hour
    if hour % 4 == 0:
        hour += 1

print(f"Time needed: {hour}h.")