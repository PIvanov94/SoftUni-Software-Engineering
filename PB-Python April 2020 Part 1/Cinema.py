screening_type = input()
rows = int(input())
columns = int(input())

cnm_capacity = rows * columns
income = 0

if screening_type == "Premiere":
    income = cnm_capacity * 12
elif screening_type == "Normal":
    income = cnm_capacity * 7.5
elif screening_type == "Discount":
    income = cnm_capacity * 5

print(f"{income:.2f} leva")