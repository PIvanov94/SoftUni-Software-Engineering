line = input().split()
first_word = line[0]
second_word = line[1]

min_len = min(len(first_word), len(second_word))
total = 0

for i in range(min_len):
    result = ord(first_word[i]) * ord(second_word[i])
    total += result

biggest_word = first_word

if len(second_word) > len(first_word):
    biggest_word = second_word

for i in range(min_len, len(biggest_word)):
    total += ord(biggest_word[i])

print(total)