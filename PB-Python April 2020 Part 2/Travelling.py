destination = input()
saved_money_all = 0

while destination != "End":
    budget = float(input())
    while saved_money_all < budget:
        saved_money = float(input())
        saved_money_all += saved_money
    else:
        print(f"Going to {destination}!")
        saved_money_all = 0
    destination = input()