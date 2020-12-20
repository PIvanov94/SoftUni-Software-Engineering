months = int(input())
electricity_total = 0
water_total = 0
net_total = 0
others = 0

for i in range(1, months + 1):
    electricity = float(input())
    electricity_total += electricity
    water_total += 20
    net_total += 15
    others = (electricity_total + water_total + net_total) * 1.2

average = (electricity_total + water_total + net_total + others) / months

print(f"Electricity: {electricity_total:.2f} lv")
print(f"Water: {water_total:.2f} lv")
print(f"Internet: {net_total:.2f} lv")
print(f"Other: {others:.2f} lv")
print(f"Average: {average:.2f} lv")