charity_amount = int(input())
sales = 0
counter = 0
sales_cash = 0
sales_card = 0
count_cash = 0
count_card = 0

while charity_amount > sales:
    command = input()
    counter += 1
    if command == "End":
        print("Failed to collect required money for charity.")
        break
    else:
        command = int(command)
    if counter % 2 == 0:
        if command < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            sales_card += int(command)
            sales += int(command)
            count_card += 1
    else:
        if command > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            sales_cash += int(command)
            sales += int(command)
            count_cash += 1
if sales >= charity_amount:
    print(f"Average CS: {sales_cash / count_cash:.2f}")
    print(f"Average CC: {sales_card / count_card:.2f}")