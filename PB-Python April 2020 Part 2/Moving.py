wide_free_space = int(input())
length_free_space = int(input())
height_free_space = int(input())
boxes_command = input()
boxes = 0
free_space = wide_free_space * length_free_space * height_free_space

while boxes_command != "Done":
    boxes = int(boxes_command)
    if free_space < boxes:
        break
    free_space -= boxes
    boxes_command = input()
    
if boxes_command == "Done":
    print(f"{free_space} Cubic meters left.")
else:
    print(f"No more free space! You need {boxes - free_space} Cubic meters more.")