climbers_groups_cnt = int(input())
total_persons = 0
group_one = 0
group_two = 0
group_three = 0
group_four = 0
group_five = 0

for i in range(1, climbers_groups_cnt + 1):
    persons_cnt = int(input())
    total_persons += persons_cnt
    if persons_cnt <= 5:
        group_one += persons_cnt
    elif 6 <= persons_cnt <= 12:
        group_two += persons_cnt
    elif 13 <= persons_cnt <= 25:
        group_three += persons_cnt
    elif 26 <= persons_cnt <= 40:
        group_four += persons_cnt
    elif persons_cnt >= 41:
        group_five += persons_cnt

group_one_percentages = group_one / total_persons * 100
group_two_percentages = group_two / total_persons * 100
group_three_percentages = group_three / total_persons * 100
group_four_percentages = group_four / total_persons * 100
group_five_percentages = group_five / total_persons * 100

print(f"{group_one_percentages:.2f}%")
print(f"{group_two_percentages:.2f}%")
print(f"{group_three_percentages:.2f}%")
print(f"{group_four_percentages:.2f}%")
print(f"{group_five_percentages:.2f}%")