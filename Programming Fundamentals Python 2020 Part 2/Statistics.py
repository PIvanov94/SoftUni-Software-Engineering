products = {}

command = input()

while not command == "statistics":
    product, quantity = command.split(": ")
    quantity = int(quantity)

    if product not in products:
        products[product] = quantity
    else:
        products[product] += quantity
    command = input()
print("Products in stock:")

for product_name, product_quantity in products.items():
    print(f"- {product_name}: {product_quantity}")

print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")