def chars_in_range(char1, char2):
    string_one_in_ascii = ord(first_letter)
    string_two_in_ascii = ord(second_letter)
    if string_one_in_ascii <= string_two_in_ascii:
        for char in range(string_one_in_ascii + 1, string_two_in_ascii):
            char = chr(char)
            print(char, end=" ")
    else:
        for char in range(string_two_in_ascii + 1, string_one_in_ascii):
            char = chr(char)
            print(char, end=" ")

    return chars_in_range


first_letter = input()
second_letter = input()

chars_in_range(first_letter, second_letter)