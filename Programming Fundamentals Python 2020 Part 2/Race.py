import re

participants = input().split(", ")
results = {el: 0 for el in participants}
pattern_words = r"[A-Za-z+]"
nums_pattern = r"\d"
line = input()

while not line == "end of race":
    name = re.findall(pattern_words, line)
    name = "".join(name)
    distance = re.findall(nums_pattern, line)
    sum_distance = 0
    for num in distance:
        sum_distance += int(num)
    if name in results:
        if not results[name] == 0:
            results[name] += sum_distance
        else:
            results[name] = sum_distance
    line = input()

sorted_results = dict(sorted(results.items(), key=lambda x: -x[1]))

winners = []

for name in sorted_results:
    winners.append(name)

print(f"1st place: {winners[0]}")
print(f"2nd place: {winners[1]}")
print(f"3rd place: {winners[2]}")