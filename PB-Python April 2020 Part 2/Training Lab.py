import math

width = float(input())
length = float(input())

seats_width = width / 1.2
seats_width_int = math.trunc(seats_width)

seats_length = (length - 1) / 0.7
seats_length_int = math.trunc(seats_length)

available_seats = seats_width_int * seats_length_int - 3

print(f"{available_seats:.0f}")
