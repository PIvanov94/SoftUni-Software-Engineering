jobs = input().split(", ")
task_index = int(input())

sorted_jobs = sorted([(int(value), index) for (index, value) in enumerate(jobs)])
cycles = 0

for (job, index) in sorted_jobs:
    cycles += job
    if index == task_index:
        break

print(cycles)