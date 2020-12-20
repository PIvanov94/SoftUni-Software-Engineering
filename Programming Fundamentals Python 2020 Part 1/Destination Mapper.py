import re

line = input()

pattern = r"(=|/)([A-Z][A-Za-z]{2,})\1"

matches = re.finditer(pattern, line)
cities = []

for match in matches:
    cities.append(match.group().replace("=", "").replace("/", ""))

print(f"Destinations: {', '.join(cities)}")
points = sum([len(c) for c in cities])
print(f"Travel Points: {points}")