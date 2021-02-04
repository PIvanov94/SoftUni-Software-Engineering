import re


def replace_special_chars(line):
    return re.sub(r"[-_.,!#$%^&*()<>?/|}{~:]", "@", line)


with open("text.txt", "r") as file:
    lines = file.readlines()
    for row in range(len(lines)):
        if row % 2 == 0:
            replaced_text = replace_special_chars(lines[row]).split()
            print(" ".join(replaced_text[::-1]))
