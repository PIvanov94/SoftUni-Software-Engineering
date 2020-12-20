n = int(input())

synonyms = {}

for i in range(n):
    word = input()
    synonym = input()
    if word in synonyms:
        synonyms[word].append(synonym)
    else:
        synonyms[word] = []
        synonyms[word].append(synonym)

for word, synonym in synonyms.items():
    print(f"{word} - {', '.join(synonym)}")