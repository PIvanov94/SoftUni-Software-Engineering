vehicles = input().split(", ")

commands_n = int(input())


def check_cards(items, card):
    return True if card in items else False


def is_in_range(items, ind):
    return True if ind in range(len(items)) else False


for command in range(1, commands_n + 1):
    data = input().split(", ")
    operator = data[0]
    if operator == "Add":
        card_name = data[1]
        if check_cards(vehicles, card_name):
            print("Card is already bought")
        else:
            vehicles.append(card_name)
            print("Card successfully bought")
    elif operator == "Remove":
        card_name = data[1]
        if check_cards(vehicles, card_name):
            vehicles.remove(card_name)
            print("Card successfully sold")
        else:
            print("Card not found")
    elif operator == "Remove At":
        index = int(data[1])
        if not is_in_range(vehicles, index):
            print("Index out of range")
        else:
            vehicles.pop(index)
            print("Card successfully sold")
    elif operator == "Insert":
        index = int(data[1])
        card_name = data[2]
        if is_in_range(vehicles, index) and check_cards(vehicles, card_name):
            print("Card is already bought")
        elif is_in_range(vehicles, index) and not check_cards(vehicles, card_name):
            vehicles.insert(index, card_name)
            print("Card successfully bought")
        elif not is_in_range(vehicles, index):
            print("Index out of range")

print(", ".join(vehicles))
