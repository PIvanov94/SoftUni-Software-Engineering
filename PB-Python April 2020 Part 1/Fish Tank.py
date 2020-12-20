length = int(input())
width = int(input())
height = int(input())
percentages_volume = float(input())

total_volume = length * width * height
total_liters = total_volume * 0.001
free_liters = total_liters * ((100 - percentages_volume) / 100)

print(f"{free_liters:.3f}")