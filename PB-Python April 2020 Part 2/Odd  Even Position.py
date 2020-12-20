import sys
n = int(input())
even_min_sum = sys.maxsize
even_max_sum = -sys.maxsize
even_sum = 0
odd_min_sum = sys.maxsize
odd_max_sum = -sys.maxsize
odd_sum = 0

for i in range(1, n + 1):
    number = float(input())
    if i % 2 == 0:
        even_sum += number
        if number > even_max_sum:
            even_max_sum = number
        if number < even_min_sum:
            even_min_sum = number
    else:
        odd_sum += number
        if number > odd_max_sum:
            odd_max_sum = number
        if number < odd_min_sum:
            odd_min_sum = number

print(f"OddSum={odd_sum:.2f},")

if odd_min_sum != sys.maxsize:
    print(f"OddMin={odd_min_sum:.2f},")
else:
    print("OddMin=No,")
if odd_max_sum != -sys.maxsize:
    print(f"OddMax={odd_max_sum:.2f},")
else:
    print("OddMax=No,")
print(f"EvenSum={even_sum:.2f},")
if even_min_sum != sys.maxsize:
    print(f"EvenMin={even_min_sum:.2f},")
else:
    print("EvenMin=No,")
if even_max_sum != -sys.maxsize:
    print(f"EvenMax={even_max_sum:.2f}")
else:
    print("EvenMax=No")