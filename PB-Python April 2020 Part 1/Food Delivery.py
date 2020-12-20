chicken_menus_cnt = int(input())
fish_menus_cnt = int(input())
vegetarian_menus_cnt = int(input())

chicken_menu_price = 10.35
fish_menu_price = 12.40
vegetarian_menu_price = 8.15
delivery_price = 2.50

chicken_sum_price = chicken_menus_cnt * chicken_menu_price
fish_sum_price = fish_menus_cnt * fish_menu_price
vegetarian_sum_price = vegetarian_menus_cnt * vegetarian_menu_price
total_price = chicken_sum_price + fish_sum_price + vegetarian_sum_price
dessert_price = total_price * 0.20
final_price = total_price + dessert_price + delivery_price

print(f"Total: {final_price:.2f}")