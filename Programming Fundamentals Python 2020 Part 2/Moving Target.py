targets = list(map(int, input().split()))

command = input()

while not command == "End":
    operation, index, value = command.split()
    index = int(index)
    value = int(value)
    if operation == "Shoot":
        if index in range(len(targets)):
            targets[index] -= value
            if targets[index] <= 0:
                del targets[index]
    elif operation == "Add":
        if index in range(len(targets)):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif operation == "Strike":
        if index - value >= 0 and index + value <= len(targets):
            del targets[index]
            if index - value >= 0:
                del targets[index]
            if index + value <= len(targets):
                del targets[index - 1]
        else:
            print("Strike missed!")

    command = input()

print("|".join(map(str, targets)))