def solve(a, b):
    count = 0
    num = a**0.5
    if not num == int(num):
        num = int(num + 1)
    while num * num <= b:
        count += 1
        num += 1
    print(count)

t = int(input())
for _ in range(t):
    solve(*map(int, input().split()))
