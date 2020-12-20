kozunak_cnt = int(input())
eggs_pack_12 = int(input())
cookies_kg = int(input())

kozunak_price = 3.20
eggs_price_per_pack = 4.35
cookies_price_per_kg = 5.40

kozunak_total_price = kozunak_cnt * kozunak_price
eggs_total_price = eggs_pack_12 * eggs_price_per_pack
cookies_total_price = cookies_kg * cookies_price_per_kg
eggs_paint_total_price = eggs_pack_12 * 12 * 0.15

total_price_dinner = kozunak_total_price + eggs_total_price + cookies_total_price + eggs_paint_total_price

print(f"{total_price_dinner:.2f}")