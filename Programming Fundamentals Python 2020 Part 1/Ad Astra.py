import re

data = input()

pattern = r"(#|\|)(?P<food>[a-zA-z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>[0-9][0-9]{0,3}|10000)\1"

matches = re.finditer(pattern, data)
total_calories = 0
foods = []

for match in matches:
    result = match.groupdict()
    total_calories += int(result["calories"])
    foods.append(result)

days = total_calories // 2000

print(f"You have food to last you for: {days} days!")

for food in foods:
    print(f"Item: {food['food']}, Best before: {food['date']}, Nutrition: {food['calories']}")

