old_version = input().split(".")

next_version = int("".join(old_version)) + 1

print(".".join(str(next_version)))