string_one = input()
string_two = input()

current_string = ""
previous_string = string_one

for iteration in range(len(string_one)):
    for index_str2 in range(0, iteration + 1):
        current_string += string_two[index_str2]
    for index_str1 in range(iteration + 1, len(string_one)):
        current_string += string_one[index_str1]
    if not previous_string == current_string:
        print(current_string)
    previous_string = current_string
    current_string = ""
