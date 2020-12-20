yards = float(input())
total_price = yards * 7.61
discount = total_price * 0.18
final_price = total_price - discount

print(f"The final price is: {final_price:.2f} lv.")
print(f"The discount is: {discount:.2f} lv.")