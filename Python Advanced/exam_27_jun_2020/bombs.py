from collections import deque

DATURA_BOMB_VALUE = 40
CHERRY_BOMB_VALUE = 60
SMOKE_DECOY_BOMB_VALUE = 120

bomb_effects = deque([int(el) for el in input().split(", ")])
bomb_casings = [int(el) for el in input().split(", ")]
datura_bombs = 0
cherry_bombs = 0
smoke_decoy_bombs = 0

while bomb_effects and bomb_casings:
    bomb_effect = bomb_effects[0]
    bomb_casing = bomb_casings[-1]
    if bomb_effect + bomb_casing == DATURA_BOMB_VALUE:
        datura_bombs += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    elif bomb_effect + bomb_casing == CHERRY_BOMB_VALUE:
        cherry_bombs += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    elif bomb_effect + bomb_casing == SMOKE_DECOY_BOMB_VALUE:
        smoke_decoy_bombs += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    else:
        bomb_casings[-1] -= 5
    if datura_bombs >= 3 and cherry_bombs >= 3 and smoke_decoy_bombs >= 3:
        break

if datura_bombs >= 3 and cherry_bombs >= 3 and smoke_decoy_bombs >= 3:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if not bomb_effects:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join(map(str, bomb_effects))}")

if not bomb_casings:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join(map(str, bomb_casings))}")

print(f"Cherry Bombs: {cherry_bombs}")
print(f"Datura Bombs: {datura_bombs}")
print(f"Smoke Decoy Bombs: {smoke_decoy_bombs}")