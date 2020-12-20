encrypted_message = input()

data = input()

while not data == "Decode":
    line = data.split("|")
    command = line[0]
    if command == "Move":
        n_letters = int(line[1])
        letters_to_move = encrypted_message[:n_letters]
        letters_left = encrypted_message[n_letters:]
        encrypted_message = letters_left + letters_to_move
    elif command == "Insert":
        index = int(line[1])
        value = line[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif command == "ChangeAll":
        substring = line[1]
        str_to_replace = line[2]
        encrypted_message = encrypted_message.replace(substring, str_to_replace)

    data = input()

print(f"The decrypted message is: {encrypted_message}")