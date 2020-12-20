n = int(input())

even_nums = []
odd_nums = []
positive_nums = []
negative_nums = []

for i in range(n):
    number = int(input())
    if number % 2 == 0:
        even_nums.append(number)
    if not number % 2 == 0:
        odd_nums.append(number)
    if number >= 0:
        positive_nums.append(number)
    else:
        negative_nums.append(number)

command = input()

if command == "even":
    print(even_nums)
elif command == "odd":
    print(odd_nums)
elif command == "positive":
    print(positive_nums)
elif command == "negative":
    print(negative_nums)