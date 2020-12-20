message = input().split()
new_message = []


for word in message:
    str_to_conv = ""
    string_words = []
    num_letter = [letter for letter in word if letter.isdigit()]
    letter_as_num_ascii = int("".join(map(str, num_letter)))
    str_to_conv += chr(letter_as_num_ascii)
    for index in word:
        if index.isalpha():
            string_words.append(index)
    string_words[0], string_words[-1] = string_words[-1], string_words[0]
    string_words = str_to_conv + "".join(string_words)
    new_message.append(string_words)

new_message = " ".join(new_message)

print(new_message)