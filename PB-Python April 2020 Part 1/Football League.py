stadium_cpt = int(input())
fans_cnt = int(input())

fans_in_sector_a = 0
fans_in_sector_b = 0
fans_in_sector_v = 0
fans_in_sector_g = 0

for i in range(1, fans_cnt + 1):
    sector = input()
    if sector == "A":
        fans_in_sector_a += 1
    elif sector == "B":
        fans_in_sector_b += 1
    elif sector == "V":
        fans_in_sector_v += 1
    elif sector == "G":
        fans_in_sector_g += 1

sector_a_percentages = fans_in_sector_a / fans_cnt * 100
sector_b_percentages = fans_in_sector_b / fans_cnt * 100
sector_v_percentages = fans_in_sector_v / fans_cnt * 100
sector_g_percentages = fans_in_sector_g / fans_cnt * 100
fans_percentages = fans_cnt / stadium_cpt * 100

print(f"{sector_a_percentages:.2f}%")
print(f"{sector_b_percentages:.2f}%")
print(f"{sector_v_percentages:.2f}%")
print(f"{sector_g_percentages:.2f}%")
print(f"{fans_percentages:.2f}%")

