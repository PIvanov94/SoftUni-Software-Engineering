food_in_kg = int(input())
food_in_g = food_in_kg * 1000
total_food = 0

while food_in_g >= total_food:
    command = input()
    if command == "Adopted":
        break
    total_food += int(command)

if food_in_g >= total_food:
    print(f"Food is enough! Leftovers: {food_in_g - total_food} grams")
else:
    print(f"Food is not enough. You need {abs(total_food - food_in_g)} grams more.")