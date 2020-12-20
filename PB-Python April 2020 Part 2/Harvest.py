import math

vineyard_square_meters = float(input())
grape_from_square_meter = float(input())
vine_liters_need = int(input())
workers_cnt = int(input())

total_grapes = vineyard_square_meters * grape_from_square_meter
total_vine = total_grapes * 0.4 / 2.5

if total_vine >= vine_liters_need:
    print(f"Good harvest this year! Total wine: {math.floor(total_vine)} liters.")
    vine_left = total_vine - vine_liters_need
    vine_for_one_worker = vine_left / workers_cnt
    print(f"{math.ceil(vine_left)} liters left -> {math.ceil(vine_for_one_worker)} liters per person.")
else:
    vine_need = vine_liters_need - total_vine
    print(f"It will be a tough winter! More {math.floor(vine_need)} liters wine needed.")