upper_limit_first_digit = int(input())
upper_limit_second_digit = int(input())
upper_limit_third_digit = int(input())

for number in range(2, upper_limit_first_digit + 1, 2):
    for number2 in range(2, upper_limit_second_digit + 1):
        for number3 in range(2, upper_limit_third_digit + 1, 2):
            if number2 == 2 or number2 == 3 or number2 == 5 or number2 == 7:
                print(f"{number} {number2} {number3}")
