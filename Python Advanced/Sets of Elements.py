first_set_length, second_set_length = [int(x) for x in input().split()]

first_set = []
second_set = []

for x in range(first_set_length):
    number = input()
    first_set.append(number)

for x in range(second_set_length):
    number = input()
    second_set.append(number)

result = set(first_set).intersection(second_set)

for el in result:
    print(el)