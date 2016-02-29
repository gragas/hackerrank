def solution(s):
    rev = s[::-1]
    limit = len(s) // 2 + 1 if len(s) % 2 == 1 else len(s) // 2
    for indx in range(limit):
        if s[indx] != rev[indx]:
            first = s[:indx] + s[indx+1:]
            if first == first[::-1]:
                return indx
            else:
                return len(s) - indx - 1
    return -1

t = int(input())
for _ in range(t):
    print(solution(input()))
