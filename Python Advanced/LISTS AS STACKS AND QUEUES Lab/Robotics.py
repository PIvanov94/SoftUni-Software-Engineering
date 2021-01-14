from collections import deque
from datetime import datetime, timedelta

robots_data = input().split(";")
time = datetime.strptime(input(), "%H:%M:%S")
robots = []
available_robots = deque([])

for el in robots_data:
    robot_data = el.split("-")
    robot = {'name': robot_data[0], 'processing time': int(robot_data[1]), 'available at': time}
    robots.append(robot)
    available_robots.append(robot)

product = input()
products = []
available_robots = deque(available_robots)

while not product == "End":
    products.append(product)
    product = input()

products = deque(products)
time = time + timedelta(seconds=1)

while products:
    current_product = products.popleft()
    if available_robots:
        current_robot = available_robots.popleft()
        current_robot['available at'] = time + timedelta(seconds=current_robot['processing time'])
        robot = [el for el in robots if el == current_robot][0]
        robot['available at'] = time + timedelta(seconds=current_robot['processing time'])
        print(f"{robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")
    else:
        for r in robots:
            if time >= r['available at']:
                available_robots.append(r)
        if not available_robots:
            products.append(current_product)
        else:
            current_robot = available_robots.popleft()
            current_robot['available at'] = time + timedelta(seconds=current_robot['processing time'])
            robot = [el for el in robots if el == current_robot][0]
            robot['available at'] = time + timedelta(seconds=current_robot['processing time'])
            print(f"{robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")
    time = time + timedelta(seconds=1)
