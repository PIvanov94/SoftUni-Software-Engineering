series = input().split()

command = input()

while not command == "end":
    data = command.split()
    operator = data[0]
    if operator == "reverse":
        start_index = int(data[2])
        count = int(data[4])
        series[start_index:start_index + count] = reversed(series[start_index:start_index + count])
    elif operator == "sort":
        start_index = int(data[2])
        count = int(data[4])
        series[start_index:start_index + count] = sorted(series[start_index:start_index + count])
    elif operator == "remove":
        count = int(data[1])
        del series[:count]

    command = input()

print(", ".join(series))
