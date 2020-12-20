# ед. цена торта - 45лв.
# ед. цена гофрета - 5.80лв.
# ед. цена палачинка - 3.20
# обща сума за всеки един продукт
# обща сума за един ден
# обща сума за всички дни (1/8 от сумата покрива разходите)

price_per_cake = 45
price_per_waffle = 5.80
price_per_pancake = 3.20
campaign_days = int(input())
confectioners = int(input())
number_of_cakes = int(input())
number_of_waffles = int(input())
number_of_pancakes = int(input())

cakes_price_per_day = number_of_cakes * price_per_cake
waffles_price_per_day = number_of_waffles * price_per_waffle
pancakes_price_per_day = number_of_pancakes * price_per_pancake

sum_for_day = (cakes_price_per_day + waffles_price_per_day + pancakes_price_per_day) * confectioners
sum_of_campaign = sum_for_day * campaign_days
sum_after_cover_costs = sum_of_campaign - (sum_of_campaign / 8)

print(f"{sum_after_cover_costs:.2f}")