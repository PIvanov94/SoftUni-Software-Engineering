eggs_cnt = int(input())
command = input()
eggs_buy = 0

while command != "Close":
    eggs_to_buy = int(input())
    if command == "Fill":
        eggs_cnt += eggs_to_buy
    elif command == "Buy":
        if eggs_to_buy <= eggs_cnt:
            eggs_cnt -= eggs_to_buy
            eggs_buy += eggs_to_buy
        else:
            print("Not enough eggs in store!")
            print(f"You can buy only {eggs_cnt}.")
            break
    command = input()

    if command == "Close":
        print(f"Store is closed!")
        print(f"{eggs_buy} eggs sold.")