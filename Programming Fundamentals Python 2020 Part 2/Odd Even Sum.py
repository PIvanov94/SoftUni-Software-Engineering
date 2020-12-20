def odd_and_even_sum(number):
    odd_sum = 0
    even_sum = 0

    for index in number:
        if not int(index) % 2 == 0:
            odd_sum += int(index)
        else:
            even_sum += int(index)
    return "Odd sum = {}, Even sum = {}".format(odd_sum, even_sum)


n_num = input()

print(odd_and_even_sum(n_num))