import sys

n = int(input())
max_num = -sys.maxsize
sum_numbers = 0

for i in range(1, n + 1):
    number = int(input())
    sum_numbers += number
    if number > max_num:
        max_num = number
sum_others = sum_numbers - max_num

if sum_others == max_num:
    print("Yes")
    print(f"Sum = {sum_others}")
else:
    print("No")
    print(f"Diff = {abs(sum_others - max_num)}")