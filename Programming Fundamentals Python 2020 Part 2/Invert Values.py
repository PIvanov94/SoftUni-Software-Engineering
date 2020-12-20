start_nums = input()
opposite_numbers = []

numbers = start_nums.split(" ")

for number in numbers:
    number = int(number)
    number *= -1
    opposite_numbers.append(number)

print(opposite_numbers)