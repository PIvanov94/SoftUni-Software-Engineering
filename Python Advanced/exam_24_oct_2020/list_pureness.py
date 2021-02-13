from collections import deque


def best_list_pureness(*args):
    values = deque(args[0])
    k = min(args[1], len(values))
    best_rotation = 0
    best_sum = 0
    for rotation in range(k+1):
        pureness = 0
        for (index, value) in enumerate(values):
            pureness += index * value
            if best_sum < pureness:
                best_rotation = rotation
                best_sum = pureness

        values.appendleft(values.pop())
    return f"Best pureness {best_sum} after {best_rotation} rotations"


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
