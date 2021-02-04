import re

alpha_path = r"[a-zA-z]"
punctuation_path = r"[-_.,!#$%^&*()'<>?/|}{~:]"


def get_symbols(text, pattern):
    return len(re.findall(pattern, text))


with open("text.txt", "r") as file:
    lines = file.readlines()
    counter_lines = 1
    for line in lines:
        count_alphas = get_symbols(line, alpha_path)
        count_punctuation_marks = get_symbols(line, punctuation_path)
        print(f"Line {counter_lines}: {line[:-1]} ({count_alphas})({count_punctuation_marks})")
        counter_lines += 1