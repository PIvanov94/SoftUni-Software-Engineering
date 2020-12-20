heritage_money = float(input())
year_living = int(input())

spend_money = 0
years_old = 18

for i in range(1800, year_living + 1):
    if i % 2 == 0:
        spend_money = 12000
        heritage_money -= spend_money
    else:
        spend_money = 12000 + (50 * years_old)
        heritage_money -= spend_money
    years_old += 1
    
if heritage_money >= 0:
    print(f"Yes! He will live a carefree life and will have {heritage_money:.2f} dollars left.")
else:
    print(f"He will need {abs(heritage_money):.2f} dollars to survive.")