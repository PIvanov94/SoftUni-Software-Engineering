import re
text = input()

pattern = r"([:]{2}|[*]{2})([A-Z][a-z]{2,})\1"

threshold = 1
cool_emojis = []

matches = re.finditer(pattern, text)
emojis = [e.group() for e in matches]
digits = re.findall(r"\d", text)

for n in digits:
    threshold = threshold * int(n)

for emoji in emojis:
    coolness = 0
    emoji_string = emoji[2:-2]
    for char in emoji_string:
        coolness += ord(char)
    if coolness > threshold:
        cool_emojis.append(emoji)

print(f"Cool threshold: {threshold}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")
print(*cool_emojis, sep="\n")