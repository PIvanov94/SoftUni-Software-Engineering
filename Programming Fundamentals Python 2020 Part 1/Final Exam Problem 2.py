import re

n = int(input())
pattern = r"(\*|@)(?P<tag>[A-Z][a-z]{2,})\1:\s(?P<char>\[[A-Za-z]\]\|){3}$"
values = []
chars_to_digits = []

for _ in range(n):
    message = input()
    if re.search(pattern, message):
        data = re.search(pattern, message)
        tag, char = data.group('tag', 'char')
        values.append(tag)
        chars = re.findall(r"[A-Za-z]", message)
        if chars:
            chars = chars[-3:]
            chars_to_digits = [ord(char) for char in chars]
        print(f"{''.join(values)}: {chars_to_digits[0]} {chars_to_digits[1]} {chars_to_digits[2]}")
        values = []
        chars_to_digits =[]
    else:
        print("Valid message not found!")