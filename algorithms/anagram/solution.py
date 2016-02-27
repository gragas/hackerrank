# Slow, but explicit

def solution(a, b):
    acounts = { c : a.count(c) for c in a }
    bcounts = { c : b.count(c) for c in b }
    for c in a:
        if not c in b:
            bcounts[c] = 0
    for c in b:
        if not c in a:
            acounts[c] = 0
    total = 0
    for key in acounts:
        total += abs(acounts[key] - bcounts[key])
    return total // 2

t = int(input())
for _ in range(t):
    s = input()
    if not len(s) % 2 == 0:
        print("-1")
        continue
    a = s[:len(s)//2]
    b = s[len(s)//2:]
    print(solution(a, b))
