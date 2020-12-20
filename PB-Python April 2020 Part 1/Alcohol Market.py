# крайна цена на уиски = цена + количество
# цена за ракия = ед. цена на уиски / 2
# цена за вино = 40% от цената на ракията
# цена за бира = 80% от цента на ракията
# print обща цена за всичко

whiskey_price = float(input())
beer_quantity = float(input())
wine_quantity = float(input())
rakia_quantity = float(input())
whiskey_quantity = float(input())

rakia_price = whiskey_price / 2
wine_price = rakia_price - (rakia_price * 0.4)
beer_price = rakia_price - (rakia_price * 0.8)
rakia_sum = rakia_quantity * rakia_price
wine_sum = wine_quantity * wine_price
beer_sum = beer_quantity * beer_price
whiskey_sum = whiskey_price * whiskey_quantity
total_sum = rakia_sum + wine_sum + beer_sum + whiskey_sum

print(f"{total_sum:.2f}")