n = int(input())

previous_pair_sum = 0
pair_difference = 0
max_difference = 0

for i in range(n):
    pair_sum = int(input()) + int(input())
    if i == 0:
        previous_pair_sum = pair_sum
    if pair_sum != previous_pair_sum:
        pair_difference = abs(pair_sum - previous_pair_sum)
        previous_pair_sum = pair_sum
    if pair_difference > max_difference:
        max_difference = pair_difference

if max_difference == 0:
    print(f"Yes, value={pair_sum}")
else:
    print(f"No, maxdiff={max_difference}")