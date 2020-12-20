stops = input()

data = input()

while not data == "Travel":
    line = data.split(":")
    command = line[0]
    if command == "Add Stop":
        index = int(line[1])
        string_to_insert = line[2]
        if index in range(len(stops)):
            first_half = stops[:index]
            second_half = stops[index:]
            stops = first_half + string_to_insert + second_half
        print(stops)
    elif command == "Remove Stop":
        start_index = int(line[1])
        end_index = int(line[2])
        if start_index in range(len(stops)) and end_index in range(len(stops)):
            first_half = stops[:start_index]
            second_half = stops[end_index + 1:]
            stops = first_half + second_half
        print(stops)
    elif command == "Switch":
        old_string = line[1]
        new_string = line[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
        print(stops)
    data = input()

print(f"Ready for world tour! Planned stops: {stops}")