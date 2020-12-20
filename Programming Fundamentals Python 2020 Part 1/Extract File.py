slash = chr(92)

line = input().split(slash)

file = line[-1].split(".")

print(f"File name: {file[0]}")
print(f"File extension: {file[1]}")