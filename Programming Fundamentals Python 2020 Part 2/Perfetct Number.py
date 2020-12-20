def is_perfect_number(n):
    divisors = []
    for num in range(1, number):
        if number % num == 0:
            divisors.append(num)

    if sum(divisors) == number:
        return True
    return False


number = int(input())

if is_perfect_number(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")