number_of_pencils = int(input())
number_of_markers = int(input())
liters_board_cleaner = float(input())
percentages_discount = int(input())

price_pencils = 5.80
price_markers = 7.20
price_for_liter_cleaner = 1.20

sum_for_pencils = number_of_pencils * price_pencils
sum_for_markers = number_of_markers * price_markers
sum_for_cleaner = liters_board_cleaner * price_for_liter_cleaner
total_price = sum_for_pencils + sum_for_markers + sum_for_cleaner
total_price_with_discount = total_price - (total_price * percentages_discount / 100)

print(f"{total_price_with_discount:.3f}")
