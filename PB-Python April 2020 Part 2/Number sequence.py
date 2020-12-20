import sys

smallest = sys.maxsize
biggest = -sys.maxsize
n = int(input())

for i in range(0, n):
    number = int(input())
    if number < smallest:
        smallest = number
    if number > biggest:
        biggest = number

print(f"Max number: {biggest}")
print(f"Min number: {smallest}")