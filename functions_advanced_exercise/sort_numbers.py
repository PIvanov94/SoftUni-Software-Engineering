def sort_numbers(nums):
    return sorted(nums, key=lambda x: x)


numbers = [int(num) for num in input().split()]


print(sort_numbers(numbers))