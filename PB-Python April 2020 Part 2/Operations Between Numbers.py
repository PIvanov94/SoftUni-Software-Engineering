n1 = int(input())
n2 = int(input())
operator = input()

if operator == '+':

    total = n1 + n2
    if total % 2 == 0:
        print(f'{n1} + {n2} = {total} - even')
    else:
        print(f'{n1} + {n2} = {total} - odd')
elif operator == '-':

    diff = n1 - n2
    if diff % 2 == 0:
        print(f'{n1} - {n2} = {diff} - even')
    else:
        print(f'{n1} - {n2} = {diff} - odd')
elif operator == '*':

    result = n1 * n2
    if result % 2 == 0:
        print(f'{n1} * {n2} = {result} - even')
    else:
        print(f'{n1} * {n2} = {result} - odd')
elif operator == '/':

    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
    else:
        division = n1 / n2
        print(f'{n1} / {n2} = {division:.2f}')
elif operator == '%':

    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
    else:
        leftover = n1 % n2
        print(f'{n1} % {n2} = {leftover}')