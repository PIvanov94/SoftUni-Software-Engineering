def numbers_searching(*numbers):
    nums_count = {}
    result = []
    for num in numbers:
        if num not in nums_count:
            nums_count[num] = 1
        else:
            nums_count[num] += 1
    duplicates = sorted([key for key, value in nums_count.items() if value > 1])
    missing_numbers = []

    for number in range(min(numbers), max(numbers) + 1):
        if number not in numbers:
            missing_numbers.append(number)

    result.extend(missing_numbers)
    result.append(duplicates)
    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
