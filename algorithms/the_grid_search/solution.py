def solve(R, C):
    data = []
    for _ in range(R):
        data.append(input())
    r, c = map(int, input().split())
    pattern = []
    for _ in range(r):
        pattern.append(input())
    for j in range(R - r + 1):
        for i in range(C - c + 1):
            found = True
            for indx in range(len(pattern)):
                if not pattern[indx] == data[j+indx][i:i+c]:
                    found = False
                    break
            if found:
                print("YES")
                return
    print("NO")

t = int(input())
for _ in range(t):
    R, C = map(int, input().split())
    solve(R, C)
