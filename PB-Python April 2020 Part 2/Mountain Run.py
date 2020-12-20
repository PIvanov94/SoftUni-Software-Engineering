import math

record_in_seconds = float(input())
distance = float(input())
time_in_sec_for_one_meter = float(input())

seconds_for_all_distance = distance * time_in_sec_for_one_meter
delay_time = math.floor(distance / 50) * 30
total_time = seconds_for_all_distance + delay_time

if total_time < record_in_seconds:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
else:
    print(f"No! He was {abs(record_in_seconds - total_time):.2f} seconds slower.")