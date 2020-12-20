# дължина на залата
# ширина на залата
# страна на квадратен гардероб
# правоъгълна скамейка - 10 пъти по-малка от залата
# един танцьор = 40см2
# пространство за танцьора = 7000см2
# брой танцьори, които могат да се поберат, закръглено число надолу

import math

hall_length = float(input())
hall_width = float(input())
wardrobe_side = float(input())

hall_area = hall_length * hall_width
wardrobe_all = math.pow(wardrobe_side, 2)
bench = hall_area / 10
free_space = hall_area - wardrobe_all - bench
dancers_in_hall = free_space / 0.704

print(math.floor(dancers_in_hall))