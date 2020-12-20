import re

pattern = r"%(?P<name>[A-Z][a-z]*)%.*?<(?P<product>\w.*?)>.*?\|(?P<count>\d+?)\|.*?(?P<price>[+-]?([0-9]*[.])?[0-9]+)\$"

line = input()
customers = []

while not line == "end of shift":
    matches = re.finditer(pattern, line)
    customer = {}
    for match in matches:
        customer = match.groupdict()
        customers.append(customer)
    line = input()

total_price = 0

for shift in customers:
    price = int(shift['count']) * float(shift['price'])
    total_price += price
    print(f"{shift['name']}: {shift['product']} - {price:.2f}")

print(f"Total income: {total_price:.2f}")