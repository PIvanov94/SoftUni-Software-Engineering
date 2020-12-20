import math
world_record = float(input())
distance = float(input())
time_for_one_meter = float(input())

time_in_seconds = distance * time_for_one_meter
delay_time = math.floor(distance / 15) * 12.5
total_time = time_in_seconds + delay_time

if total_time < world_record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    need_seconds = total_time - world_record
    print(f"No, he failed! He was {need_seconds:.2f} seconds slower.")