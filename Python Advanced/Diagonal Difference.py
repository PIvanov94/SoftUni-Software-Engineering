n = int(input())

matrix = []

for _ in range(n):
    elements = [int(el) for el in input().split()]
    matrix.append(elements)

sum_first_diagonal = 0
sum_second_diagonal = 0
columns = n - 1

for i in range(n):
    sum_first_diagonal += matrix[i][i]
    sum_second_diagonal += matrix[i][columns]
    columns -= 1

print(abs(sum_first_diagonal - sum_second_diagonal))