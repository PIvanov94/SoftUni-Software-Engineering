items = input().split(", ")
command = input()


def check_for_item(item, items):
    if item in items:
        return True
    else:
        return False


while not command == "Craft!":
    command, item = command.split(" - ")

    if command == "Collect":
        if not check_for_item(item, items):
            items.append(item)
    elif command == "Drop":
        if check_for_item(item, items):
            items.remove(item)
    elif command == "Combine Items":
        old_item, new_item = item.split(":")
        if check_for_item(old_item, items):
            index = items.index(old_item)
            items.insert(index + 1, new_item)
    elif command == "Renew":
        if check_for_item(item, items):
            items.remove(item)
            items.append(item)

    command = input()

print(", ".join(items))