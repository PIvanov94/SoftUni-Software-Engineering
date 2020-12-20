targets = list(map(int, input().split()))

command = input()
shot_targets = 0

while not command == "End":
    shot_index = int(command)
    if shot_index in range(len(targets)):
        current_num = targets[shot_index]
        for i in range(len(targets)):
            if not targets[i] == -1:
                if targets[i] > current_num:
                    targets[i] -= current_num
                else:
                    targets[i] += current_num
        targets[shot_index] = -1
        shot_targets += 1
    command = input()
else:
    print(f"Shot targets: {shot_targets} -> {' '.join(map(str, targets))}")