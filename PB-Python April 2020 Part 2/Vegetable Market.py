price_for_kg_vegetables_in_bgn = float(input())
price_for_kg_fruits_in_bgn = float(input())
total_kgs_vegetables = float(input())
total_kgs_fruits = float(input())

total_price_vegetables_in_bgn = total_kgs_vegetables * price_for_kg_vegetables_in_bgn
total_price_fruits_in_bgn = total_kgs_fruits * price_for_kg_fruits_in_bgn
sum_price_in_euros = (total_price_vegetables_in_bgn + total_price_fruits_in_bgn) / 1.94

print(f"{sum_price_in_euros:.2f}")