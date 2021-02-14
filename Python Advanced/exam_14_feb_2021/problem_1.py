from collections import deque

firework_effects = deque([int(el) for el in input().split(", ")])
explosive_power = [int(el) for el in input().split(", ")]

palm = 0
willow = 0
crossette = 0

while firework_effects and explosive_power:
    effect = firework_effects[0]
    power = explosive_power[-1]
    sum_firework = effect + power
    if effect <= 0:
        firework_effects.popleft()
        continue
    if power <= 0:
        explosive_power.pop()
        continue
    if sum_firework % 3 == 0 and not sum_firework % 5 == 0:
        palm += 1
        firework_effects.popleft()
        explosive_power.pop()
    elif sum_firework % 5 == 0 and not sum_firework % 3 == 0:
        willow += 1
        firework_effects.popleft()
        explosive_power.pop()
    elif sum_firework % 3 == 0 and sum_firework % 5 == 0:
        crossette += 1
        firework_effects.popleft()
        explosive_power.pop()
    else:
        effect -= 1
        firework_effects.append(effect)
        firework_effects.popleft()
    if palm >= 3 and willow >= 3 and crossette >= 3:
        break
    if not firework_effects or not explosive_power:
        break

if palm >= 3 and willow >= 3 and crossette >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can’t make the perfect firework show.")
if firework_effects:
    print(f"Firework Effects left: {', '.join(map(str, firework_effects))}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(map(str, explosive_power))}")

print(f"Palm Fireworks: {palm}")
print(f"Willow Fireworks: {willow}")
print(f"Crossette Fireworks: {crossette}")