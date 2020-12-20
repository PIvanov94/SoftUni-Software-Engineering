import sys

n = int(input())
count = 0
max_number = -sys.maxsize

while count < n:
    number = int(input())
    if number > max_number:
        max_number = number
    count += 1

print(max_number)