divisor = int(input())
bound = int(input())
largest_number = 0

for n in range(bound + 1):
    if n % divisor == 0:
        if n <= bound:
            if n > 0:
                largest_number = n

print(largest_number)