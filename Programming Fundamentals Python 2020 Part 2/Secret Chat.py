concealed_message = input()

data = input()

while not data == "Reveal":
    line = data.split(":|:")
    command = line[0]
    if command == "InsertSpace":
        index = int(line[1])
        first_part = concealed_message[:index]
        second_part = concealed_message[index:]
        concealed_message = first_part + " " + second_part
        print(concealed_message)
    elif command == "Reverse":
        substring = line[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, "", 1)
            substring = substring[::-1]
            concealed_message = concealed_message + substring
            print(concealed_message)
        else:
            print("error")
    elif command == "ChangeAll":
        substring = line[1]
        replacement = line[2]
        concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)

    data = input()

print(f"You have a new text message: {concealed_message}")