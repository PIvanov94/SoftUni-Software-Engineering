n_lines = int(input())

result = 0

for line in range(1, n_lines + 1):
    letter = input()
    result += ord(letter)

print(f"The sum equals: {result}")