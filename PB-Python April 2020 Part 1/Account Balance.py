n = int(input())
counter = 0
total = 0

while counter < n:
    increase = float(input())
    if increase < 0:
        print("Invalid operation!")
        break

    total += increase
    print(f"Increase: {increase:.2f}")
    counter += 1

print(f"Total: {total:.2f}")