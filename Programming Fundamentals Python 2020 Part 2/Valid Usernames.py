usernames = input().split(", ")
allowed_chars = set("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-")
valid_usernames = []

for username in usernames:
    validation = set(username)
    if 3 <= len(username) <= 16 and validation.issubset(allowed_chars):
        valid_usernames.append(username)

for name in valid_usernames:
    print(name)