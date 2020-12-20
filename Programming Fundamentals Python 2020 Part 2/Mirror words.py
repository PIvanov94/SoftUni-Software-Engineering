import re

data = input()

pattern = r'(#|@)[a-zA-z]{3,}\1{2}[a-zA-Z]{3,}\1'

matches = re.finditer(pattern, data)
pairs = []
mirror_words = []

for match in matches:
    pairs.append(match.group().replace('@', '').replace('#', ''))

for word in pairs:
    word1 = word[:len(word) // 2]
    word2 = word[len(word) // 2:]
    word2_rev = word2[::-1]
    if word1 == word2_rev:
        mirror_words.append(word1 + ' <=> ' + word2)

if not pairs:
    print("No word pairs found!")
else:
    print(f"{len(pairs)} word pairs found!")

if not mirror_words:
    print('No mirror words!')
else:
    print('The mirror words are:')
    print(', '.join(mirror_words))