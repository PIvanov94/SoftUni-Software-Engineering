password = input()

line = input()
new_password = ""

while not line == "Done":
    data = line.split()
    command = data[0]
    if command == "TakeOdd":
        for i in range(1, len(password), 2):
            new_password += password[i]
        password = new_password
        print(password)
    elif command == "Cut":
        index = int(data[1])
        length = int(data[2])
        password = password[:index] + password[index+length:]
        print(password)
    elif command == "Substitute":
        substring = data[1]
        substitute = data[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")
    line = input()

print(f"Your password is: {password}")