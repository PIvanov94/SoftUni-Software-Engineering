import sys

kozunak_cnt = int(input())
max_chef_grades = -sys.maxsize
top_chef = ""

for kozunak in range(1, kozunak_cnt + 1):
    chef_name = input()
    total_points = 0

    while chef_name != "Stop":
        rating = input()

        if rating == "Stop":
            print(f"{chef_name} has {total_points} points.")
            break

        total_points += int(rating)
    if total_points > max_chef_grades:
        max_chef_grades = total_points
        top_chef = chef_name
        print(f"{top_chef} is the new number 1!")

print(f"{top_chef} won competition with {max_chef_grades} points!")