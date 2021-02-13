def list_manipulator(*args):
    numbers = list(args[0])
    command = args[1]
    place = args[2]
    if command == "add" and place == "beginning":
        number_to_insert = [int(num) for num in args[3:]]
        numbers.insert(0, number_to_insert)
        numbers = [num for sublist in numbers for num in sublist]
    elif command == "add" and place == "end":
        number_to_insert = [int(num) for num in args[3:]]
        numbers.extend(number_to_insert)
    return numbers


