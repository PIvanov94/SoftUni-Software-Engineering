import re

data = input()

pattern = r"\d+"
digits = []

while data:
    match = re.findall(pattern, data)
    if match:
        digits.extend(match)
    data = input()

print(*digits)