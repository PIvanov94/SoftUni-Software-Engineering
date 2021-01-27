numbers = [int(el) for el in input().split(", ")]

print(f"Positive: ", end="")
print(*[num for num in numbers if num >= 0], sep=", ")
print(f"Negative: ", end="")
print(*[num for num in numbers if num < 0], sep=", ")
print(f"Even: ", end="")
print(*[num for num in numbers if num % 2 == 0], sep=", ")
print(f"Odd: ", end="")
print(*[num for num in numbers if not num % 2 == 0], sep=", ")
