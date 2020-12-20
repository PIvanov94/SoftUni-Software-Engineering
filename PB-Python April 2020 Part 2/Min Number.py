import sys

n = int(input())
count = 0
min_number = sys.maxsize

while count < n:
    number = int(input())
    if number < min_number:
        min_number = number
    count += 1
    
print(min_number)