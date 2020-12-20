painted_eggs_cnt = int(input())
red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0
max_eggs = 0
colour = ""

for egg in range(1, painted_eggs_cnt + 1):
    colour = input()
    if colour == "red":
        red_eggs += 1
    elif colour == "orange":
        orange_eggs += 1
    elif colour == "blue":
        blue_eggs += 1
    elif colour == "green":
        green_eggs += 1

check1 = red_eggs > orange_eggs and red_eggs > blue_eggs and red_eggs > green_eggs
check2 = orange_eggs > red_eggs and orange_eggs > blue_eggs and orange_eggs > green_eggs
check3 = blue_eggs > red_eggs and blue_eggs > orange_eggs and blue_eggs > green_eggs
check4 = green_eggs > red_eggs and green_eggs > orange_eggs and green_eggs > blue_eggs

if check1:
    max_eggs = red_eggs
    colour = "red"
elif check2:
    max_eggs = orange_eggs
    colour = "orange"
elif check3:
    max_eggs = blue_eggs
    colour = "blue"
elif check4:
    max_eggs = green_eggs
    colour = "green"

print(f"Red eggs: {red_eggs}")
print(f"Orange eggs: {orange_eggs}")
print(f"Blue eggs: {blue_eggs}")
print(f"Green eggs: {green_eggs}")
print(f"Max eggs: {max_eggs} -> {colour}")