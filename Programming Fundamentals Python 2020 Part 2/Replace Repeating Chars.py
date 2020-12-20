line = input()
text = ""
new_letter = ""

for letter in line:
    if not letter == new_letter:
        text += letter
    new_letter = letter

print(text)