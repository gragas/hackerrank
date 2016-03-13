def solution(c, m):
    for i, val1 in enumerate(c):
        for j, val2 in enumerate(c[i+1:]):
            if val1 + val2 == m:
                print("{} {}".format(i+1, i+1+j+1))
                return

t = int(input())

for _ in range(t):
    m = int(input())
    n = int(input())
    c = list(map(int, input().split()))
    solution(c, m)
