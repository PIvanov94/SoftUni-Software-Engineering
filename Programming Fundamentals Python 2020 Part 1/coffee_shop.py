orders_cnt = int(input())
total_price = 0
for order in range(orders_cnt):
    price_per_capsule = float(input())
    days = int(input())
    capsules_cnt = int(input())
    order_price = (days * capsules_cnt) * price_per_capsule
    total_price += order_price
    print(f"The price for the coffee is: ${order_price:.2f}")

print(f"Total: ${total_price:.2f}")