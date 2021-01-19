n = int(input())
intersections = []

for _ in range(n):
    data = input()
    first_seq_data, second_seq_data = data.split("-")
    start, stop = [int(el) for el in first_seq_data.split(",")]
    first_sequence = range(start, stop + 1)
    start_2, stop_2 = [int(el) for el in second_seq_data.split(",")]
    second_sequence = range(start_2, stop_2 + 1)
    intersection = set(first_sequence).intersection(second_sequence)
    intersections.append(intersection)

longest_intersection = sorted(intersections, key=lambda x: -len(x))[0]

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")