import re

pattern = r">>(?P<name>[A-Za-z]+)<<(?P<price>[-+]?[0-9]*\.?[0-9]*)!(?P<quantity>\d+)"

lines = input()
furniture = []
total_price = 0
while not lines == "Purchase":
    if re.match(pattern, lines):
        data = re.search(pattern, lines)
        name, price, quantity = data.group('name', 'price', 'quantity')
        furniture.append(name)
        total_price += float(price) * int(quantity)

    lines = input()

print("Bought furniture:")
[print(item)for item in furniture]
print(f"Total money spend: {total_price:.2f}" )