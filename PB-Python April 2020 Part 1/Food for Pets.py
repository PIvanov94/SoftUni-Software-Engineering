import math

days_cnt = int(input())
food_total = float(input())
total_dog_food = 0
total_cat_food = 0
current_biscuits = 0
biscuits = 0

for i in range(1, days_cnt + 1):
    dog_food = int(input())
    cat_food = int(input())
    total_dog_food += dog_food
    total_cat_food += cat_food

    if i % 3 == 0:
        current_biscuits = (dog_food + cat_food) * 0.1
        biscuits += current_biscuits

total_food_all = total_dog_food + total_cat_food
total_food_percentages = total_food_all / food_total * 100
dog_food_percentages = (total_dog_food / total_food_all) * 100
cat_food_percentages = (total_cat_food / total_food_all) * 100

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{total_food_percentages:.2f}% of the food has been eaten.")
print(f"{dog_food_percentages:.2f}% eaten from the dog.")
print(f"{cat_food_percentages:.2f}% eaten from the cat.")