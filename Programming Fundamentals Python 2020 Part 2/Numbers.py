numbers = list(map(int, input().split()))

average_num = sum(numbers) / len(numbers)

greater_num = [num for num in numbers if num > average_num]
greater_num = sorted(greater_num, reverse=True)

if len(greater_num) > 5:
    greater_num = greater_num[0:5]

if not greater_num:
    print("No")
else:
    print(" ".join(map(str, greater_num)))