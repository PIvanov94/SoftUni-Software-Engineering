def print_sum_numbers(nums):
    sum_negative_numbers = sum([num for num in nums if num < 0])
    sum_positive_numbers = sum([num for num in nums if num > 0])
    print(sum_negative_numbers, sum_positive_numbers, sep="\n")
    if sum_positive_numbers > abs(sum_negative_numbers):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


numbers = [int(num) for num in input().split()]

print_sum_numbers(numbers)