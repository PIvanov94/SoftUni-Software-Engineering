import re

data = input()

pattern = r"(^|(?<=\s))[A-Za-z0-9]+[\._-]?[A-Za-z0-9]+@[A-Za-z]+\-?[A-Za-z]+(\.[A-Za-z]+\-?[A-Za-z]+)+"

result = re.finditer(pattern, data)

for el in result:
    print(el.group())
