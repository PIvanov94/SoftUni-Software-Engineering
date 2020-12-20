command = input()

c_counter = 0
o_counter = 0
n_counter = 0
word = ""
word_to_print = ""

while command != "End":
    letter = command
    if ("a" <= letter <= 'z') or ('A' <= letter <= 'Z'):
        if letter == "c" and c_counter == 0:
            c_counter += 1
        elif letter == "o" and o_counter == 0:
            o_counter += 1
        elif letter == "n" and n_counter == 0:
            n_counter += 1
        else:
            word += letter
        if c_counter != 0 and o_counter != 0 and n_counter != 0:
            c_counter = 0
            o_counter = 0
            n_counter = 0
            word_to_print += word
            word_to_print += " "
            word = ""
    command = input()

print(word_to_print)
