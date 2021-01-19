n = int(input())
usernames = []

for _ in range(n):
    username = input()
    usernames.append(username)

unique_usernames = set(usernames)

for el in unique_usernames:
    print(el)