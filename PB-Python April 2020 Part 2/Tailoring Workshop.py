# брой правоъгълни маси
# дължина на масите
# ширина на масите
# размер на покривки = дължина + ширина на масите + 120
# карета = дължина на маса / 2
# долар = 1.85

tables_all = int(input())
tables_length = float(input())
tables_width = float(input())

covers = tables_all * (tables_length + 2 * 0.30) * (tables_width + 2 * 0.30)
squares = tables_all * (tables_length / 2 * tables_length / 2)
covers_price_per_meter = 7
squares_price_per_meter = 9
price_usd = covers * covers_price_per_meter + squares * squares_price_per_meter
price_bgn = price_usd * 1.85

print(f"{price_usd:.2f} USD")
print(f"{price_bgn:.2f} BGN")


