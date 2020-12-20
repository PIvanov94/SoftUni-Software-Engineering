number = float(input())
unit = str(input())
result_unit = str(input())

if unit == "mm":
    number /= 1000
elif unit == "cm":
    number /= 100
if result_unit == "mm":
    number *= 1000
elif result_unit == "cm":
    number *= 100

print(f"{number:.3f}")