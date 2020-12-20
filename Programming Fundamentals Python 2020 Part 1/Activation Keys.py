activation_key = input()

data = input()

while not data == "Generate":
    data = data.split(">>>")
    command = data[0]
    if command == "Contains":
        substring = data[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif command == "Flip":
        case = data[1]
        start_index = int(data[2])
        end_index = int(data[3])
        first_part = activation_key[:start_index]
        second_part = activation_key[end_index:]
        part_to_change = activation_key[start_index:end_index]
        if case == "Upper":
            part_to_change = part_to_change.upper()
        elif case == "Lower":
            part_to_change = part_to_change.lower()
        activation_key = first_part + part_to_change + second_part
        print(activation_key)
    elif command == "Slice":
        start_index = int(data[1])
        end_index = int(data[2])
        first_part = activation_key[:start_index]
        second_part = activation_key[end_index:]
        activation_key = first_part + second_part
        print(activation_key)
    data = input()

print(f"Your activation key is: {activation_key}")