number_of_bitcoins = int(input())
number_of_chinese_yuan = float(input())
percentages_commission = float(input())

bitcoin_to_bgn = 1168
yuan_to_usd = 0.15
usd_to_bgn = 1.76
euro_to_bgn = 1.95

sum_for_bitcoins_in_bgn = number_of_bitcoins * bitcoin_to_bgn
sum_for_chinese_yuan_in_usd = number_of_chinese_yuan * yuan_to_usd
sum_for_chinese_yuan_in_bgn = sum_for_chinese_yuan_in_usd * usd_to_bgn
sum_in_euros = (sum_for_bitcoins_in_bgn + sum_for_chinese_yuan_in_bgn) / euro_to_bgn
sum_commission = sum_in_euros * (percentages_commission / 100)
total_sum = sum_in_euros - sum_commission

print(f"{total_sum:.2f}")