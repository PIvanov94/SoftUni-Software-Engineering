data = input().split()
dictionary = {}

for element in data:
    for letter in element:
        dictionary[letter] = dictionary.setdefault(letter, 0) + 1

for letter, occurrence in dictionary.items():
    print(f"{letter} -> {occurrence}")