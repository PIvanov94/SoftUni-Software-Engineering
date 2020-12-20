number = int(input())
message = ""

for sheep in range(number):
    message += f"{sheep + 1} sheep..."

print(message)