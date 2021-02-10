from collections import deque

males = [int(el) for el in input().split()]
females = [int(el) for el in input().split()]
females = deque(females)
matches = 0

while females and males:
    female = females[0]
    male = males[-1]
    if female <= 0:
        females.popleft()
        continue
    elif male <= 0:
        males.pop()
        continue
    elif male % 25 == 0:
        males.pop()
        continue
    elif female % 25 == 0:
        females.popleft()
        continue
    if female == male:
        males.pop()
        females.popleft()
        matches += 1
    else:
        males[-1] -= 2
        females.popleft()


print(f"Matches: {matches}")

if males:
    print(f"Males left: {', '.join(map(str, reversed(males)))}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join(map(str, females))}")
else:
    print("Females left: none")
