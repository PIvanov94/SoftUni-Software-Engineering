def pass_validator(password):
    is_valid = True

    if not (6 <= len(password) <= 10):
        is_valid = False
        print("Password must be between 6 and 10 characters")
    counter_digits = 0
    for el in password:
        if not el.isdigit() and not el.isalpha():
            is_valid = False
            print("Password must consist only of letters and digits")
            break
        if el.isdigit():
            counter_digits += 1
    if counter_digits < 2:
        is_valid = False
        print("Password must have at least 2 digits")
    return is_valid


password = input()
result = pass_validator(password)

if result:
    print("Password is valid")