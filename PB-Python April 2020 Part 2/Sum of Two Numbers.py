start_number = int(input())
end_number = int(input())
magic_number = int(input())
counter = 0
found = False

for x in range(start_number, end_number + 1):
    for y in range(start_number, end_number + 1):
        res = x + y
        counter += 1
        if res == magic_number:
            print(f"Combination N:{counter} ({x} + {y} = {magic_number})")
            found = True
            break
    if found:
        break

if not found:
    print(f"{counter} combinations - neither equals {magic_number}")