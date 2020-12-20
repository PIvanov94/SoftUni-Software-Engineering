import re

data = input()

pattern = r"((?<=^_)|(?<=\s_))[a-zA-Z0-9]+\b"

result = [name.group() for name in re.finditer(pattern, data)]

print(",".join(result))