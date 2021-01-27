rows, cols = [int(el) for el in input().split()]

result = [[f"{chr(num)}{chr(n)}{chr(num)}"for n in range(num, num+cols)] for num in range(97, 97+rows)]

[print(*r) for r in result]