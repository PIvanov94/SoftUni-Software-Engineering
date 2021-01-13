clothes_in_box = list(map(int, input().split()))
rack = int(input())

racks_counter = 1
current_rack_capacity = rack

while clothes_in_box:
    current_v_cloth = clothes_in_box.pop()
    if current_v_cloth <= current_rack_capacity:
        current_rack_capacity -= current_v_cloth
    else:
        racks_counter += 1
        current_rack_capacity = rack
        current_rack_capacity -= current_v_cloth

print(racks_counter)