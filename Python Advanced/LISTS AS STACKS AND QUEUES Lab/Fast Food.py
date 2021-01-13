from collections import deque

food_quantity = int(input())
orders_quantity = list(map(int, input().split()))
orders = deque()

for order in orders_quantity:
    orders.append(order)
print(max(orders_quantity))

while orders:
    order = int(orders.popleft())
    if order <= food_quantity:
        food_quantity -= order
    else:
        orders.append(order)
        print(f"Orders left: {order}")
        break
    if not orders:
        print("Orders complete")