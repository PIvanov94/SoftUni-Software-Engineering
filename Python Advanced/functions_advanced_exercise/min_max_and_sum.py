def find_min_number(numbers):
    return min(numbers)


def find_max_number(numbers):
    return max(numbers)


def sum_numbers(numbers):
    return sum(numbers)


nums = [int(num) for num in input().split()]

print(f"The minimum number is {find_min_number(nums)}")
print(f"The maximum number is {find_max_number(nums)}")
print(f"The sum number is: {sum_numbers(nums)}")