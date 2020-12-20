data = input()
products_prices = {}
products_quantities = {}

while not data == "buy":
    product, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)
    if product not in products_quantities:
        products_quantities[product] = quantity
    else:
        products_quantities[product] += quantity
    products_prices[product] = price
    data = input()

result = {key: products_quantities[key] * products_prices.get(key, 0) for key in products_quantities.keys()}

for product, price in result.items():
    print(f"{product} -> {price:.2f}")