text = input()
line = input()

while not line == "Finish":
    data = line.split()
    command = data[0]
    if command == "Replace":
        current_char = data[1]
        new_char = data[2]
        text = text.replace(current_char, new_char)
        print(text)
    elif command == "Cut":
        start_index = int(data[1])
        end_index = int(data[2])
        if start_index in range(len(text)) and end_index in range(len(text)):
            fist_half = text[:start_index]
            second_half = text[end_index + 1:]
            text = fist_half + second_half
            print(text)
        else:
            print("Invalid indices!")
    elif command == "Make":
        method = data[1]
        if method == "Upper":
            text = text.upper()
        elif method == "Lower":
            text = text.lower()
        print(text)
    elif command == "Check":
        string = data[1]
        if string in text:
            print(f"Message contains {string}")
        else:
            print(f"Message doesn't contain {string}")
    elif command == "Sum":
        start_index = int(data[1])
        end_index = int(data[2])
        if start_index in range(len(text)) and end_index in range(len(text)):
            substring = text[start_index:end_index+1]
            substring = sum([ord(char) for char in substring])
            print(substring)
        else:
            print("Invalid indices!")

    line = input()
