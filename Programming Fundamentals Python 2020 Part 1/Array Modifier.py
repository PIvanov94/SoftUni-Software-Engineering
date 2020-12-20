numbers = list(map(int, input().split()))

command = input()

while not command == "end":
    command_type = command.split()[0]
    if command_type == "decrease":
        numbers = [num - 1 for num in numbers]
    if command_type == "swap":
        index_one = int(command.split()[1])
        index_two = int(command.split()[2])
        numbers[index_one], numbers[index_two] = numbers[index_two], numbers[index_one]
    elif command_type == "multiply":
        index_one = int(command.split()[1])
        index_two = int(command.split()[2])
        numbers[index_one] *= numbers[index_two]

    command = input()

print(", ".join(map(str, numbers)))