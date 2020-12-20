words = input().split()

alphabet_lower = {chr(ele+97): ele+1 for ele in range(26)}
total = 0

for word in words:
    first_letter = word[0]
    last_letter = word[-1]
    number = int(word[1:-1])
    if first_letter.isupper():
        number /= alphabet_lower[first_letter.lower()]
    else:
        number *= alphabet_lower[first_letter.lower()]
    if last_letter.isupper():
        number -= alphabet_lower[last_letter.lower()]
    else:
        number += alphabet_lower[last_letter.lower()]
    total += number

print(f"{total:.2f}")