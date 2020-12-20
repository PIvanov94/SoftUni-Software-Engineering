height_house = float(input())
length_house = float(input())
height_roof = float(input())

side_wall_of_house = height_house * length_house
window = 1.5 * 1.5
sum_wallsides_of_house = (side_wall_of_house * 2) - (window * 2)
backside_house = height_house * height_house
entrance = 1.2 * 2
sum_backsides_house = (backside_house * 2) - entrance
total_area_house = sum_wallsides_of_house + sum_backsides_house
green_paint = total_area_house / 3.4

wallside_roof = 2 * side_wall_of_house
frontside_roof = 2 * (height_house * height_roof / 2)
total_area_roof = wallside_roof + frontside_roof
red_paint = total_area_roof / 4.3

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")