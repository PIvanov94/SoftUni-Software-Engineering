def filter_even_numbers(nums):
    return list(filter(lambda x: x % 2 == 0, nums))


numbers = [int(num) for num in input().split()]

print(filter_even_numbers(numbers))