tournament_days = int(input())
win_games = 0
lose_games = 0
total_money = 0

for i in range(1, tournament_days + 1):
    command = input()
    raised_money_day = 0
    win_games_day = 0
    lose_games_day = 0
    while command != "Finish":
        command = input()
        if command == "win":
            raised_money_day += 20
            win_games += 1
            win_games_day += 1
        elif command == "lose":
            lose_games += 1
            lose_games_day += 1
        command = input()
    if win_games_day > lose_games_day:
        raised_money_day *= 1.1
    total_money += raised_money_day

if win_games > lose_games:
    total_money *= 1.2
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")