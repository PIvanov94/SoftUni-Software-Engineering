flat = [[el for el in l.split()] for l in input().split("|")]

print(*[" ".join(el) for el in flat[::-1]])