rooms = int(input())
free_chairs = 0
needed_chairs = 0

for room in range(1, rooms+1):
    charis, taken_chairs = input().split()
    chairs_as_num = len(charis)

    if int(taken_chairs) < chairs_as_num:
        free_chairs += int(chairs_as_num) - int(taken_chairs)
    elif int(taken_chairs) > chairs_as_num:
        needed_chairs += abs(chairs_as_num - int(taken_chairs))
        print(f"{abs(chairs_as_num - int(taken_chairs))} more chairs needed in room {room}")


if free_chairs >= needed_chairs:
    free_chairs -= needed_chairs
    print(f"Game On, {free_chairs} free chairs left")