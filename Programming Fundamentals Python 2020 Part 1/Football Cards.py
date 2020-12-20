cards = input()
cards_as_list= cards.split(" ")

team_a = 11
team_b = 11
term_game = False

for element in set(cards_as_list):
    team, player = element.split("-")
    if team == "A":
        team_a -= 1
    elif team == "B":
        team_b -= 1
    if team_a < 7 or team_b < 7:
        term_game = True
        break

print(f"Team A - {team_a}; Team B - {team_b}")

if term_game:
    print("Game was terminated")