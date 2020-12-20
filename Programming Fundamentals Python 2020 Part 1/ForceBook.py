line = input()

sides = {}

while not line == "Lumpawaroo":
    if '|' in line:
        force_side, force_user = line.split(" | ")
        if force_user not in sides:
            sides[force_side] = [force_user]
        else:
            sides[force_side].append(force_user)
    elif "->" in line:
        force_user, force_side = line.split(" -> ")
        for side, users in sides.items():
            if force_user in users:
                users.remove(force_user)
            if force_side not in sides:
                sides[force_side] = [force_user]
            else:
                sides[force_side].append(force_user)
    else:
        break

    line = input()
