import math

numbers = input().split(", ")
nums = list(map(int, numbers))
BOUNDARY = 10

for i in range(1, math.ceil(max(nums) / 10) + 1):
    result = [nums[number] for number in range(len(nums)) if nums[number] in range(i * 10 - 10 + 1, i * 10 + 1)]
    print(f"Group of {i * BOUNDARY}'s: {result}")