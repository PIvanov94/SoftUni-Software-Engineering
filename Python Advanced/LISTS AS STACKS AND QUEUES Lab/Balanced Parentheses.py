parentheses = input()
is_balanced = True
opening = []
mapper = {'{': '}', '(': ')', '[': ']'}
for p in parentheses:
    if p in "({[":
        opening.append(p)
    else:
        if not opening:
            is_balanced = False
            break
        current_opening_b = opening.pop()
        if not mapper[current_opening_b] == p:
            is_balanced = False
            break
if is_balanced:
    print("YES")
else:
    print("NO")