words = input().split()

dictionary = {}
words = [word.lower() for word in words]

for word in words:
    dictionary[word] = words.count(word)

for key, value in dictionary.items():
    if not value % 2 == 0:
        print(key, end=" ")