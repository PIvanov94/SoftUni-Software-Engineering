line = input().split(">")
power = 0
final_line = []

for index in line:
    if index[0].isdigit():
        power += int(index[0])
        if len(index) <= power:
            power -= len(index)
            index = ">"
        else:
            index = ">"+"".join(list(index[power::]))
            power = 0
    final_line.append(index)

print("".join(final_line))