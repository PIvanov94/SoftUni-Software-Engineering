n = int(input())

heroes = {}

for _ in range(n):
    name, hp, mp = input().split()
    hp = int(hp)
    mp = int(mp)
    heroes[name] = {"HP": hp, "MP": mp}

line = input()

while not line == "End":
    data = line.split(" - ")
    command = data[0]
    hero_name = data[1]
    if command == "CastSpell":
        mp_needed = int(data[2])
        spell_name = data[3]
        current_mana_points = heroes[hero_name]["MP"]
        if mp_needed > current_mana_points:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
        else:
            heroes[hero_name]["MP"] = current_mana_points - mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['MP']} MP!")
    elif command == "TakeDamage":
        damage = int(data[2])
        attacker = data[3]
        life_points_left = heroes[hero_name]["HP"] - damage
        if life_points_left <= 0:
            del heroes[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")
        else:
            heroes[hero_name]["HP"] = life_points_left
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['HP']} HP left!")
    elif command == "Recharge":
        amount = int(data[2])
        current_mana_points = heroes[hero_name]["MP"]
        if heroes[hero_name]["MP"] + amount >= 200:
            heroes[hero_name]["MP"] = 200
            print(f"{hero_name} recharged for {200 - current_mana_points} MP!")
        else:
            heroes[hero_name]["MP"] += amount
            print(f"{hero_name} recharged for {amount} MP!")
    elif command == "Heal":
        amount = int(data[2])
        current_health_points = heroes[hero_name]["HP"]
        if heroes[hero_name]["HP"] + amount >= 100:
            heroes[hero_name]["HP"] = 100
            print(f"{hero_name} healed for {100 - current_health_points} HP!")
        else:
            heroes[hero_name]["HP"] += amount
            print(f"{hero_name} healed for {amount} HP!")

    line = input()

ordered_heroes = sorted(heroes.items(), key=lambda x: (-x[1]["HP"], x[0]))

for name, value in ordered_heroes:
    print(name)
    print(f"  HP: {value['HP']}")
    print(f"  MP: {value['MP']}")