def solve(width, i, j):
    print(min(width[i:j+1]))

n, t = map(int, input().split())
width = list(map(int, input().split()))
for _ in range(t):
    i, j = map(int, input().split())
    solve(width, i, j)
