numbers = list(map(int, input().split()))

s = []
result = []
for n in numbers:
    s.append(n)

while s:
    num = s.pop()
    result.append(num)

print(*result)