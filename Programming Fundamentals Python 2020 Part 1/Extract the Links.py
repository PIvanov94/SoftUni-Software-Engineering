import re

text = input()
pattern = r"(w{3}).([A-Za-z0-9-]+)(\.[a-z]+)+"

while text:
    for el in re.finditer(pattern, text):
        print(el.group())
    text = input()