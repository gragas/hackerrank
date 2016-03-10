def solution(dollars, dollars_per_chocolate, wrappers_per_chocolate):
    total_chocolates = dollars // dollars_per_chocolate
    total_wrappers = total_chocolates
    while total_wrappers >= wrappers_per_chocolate:
        total_chocolates += total_wrappers // wrappers_per_chocolate
        remaining_wrappers = total_wrappers % wrappers_per_chocolate
        total_wrappers = remaining_wrappers + \
                         total_wrappers // wrappers_per_chocolate
    return total_chocolates

t = int(input())
for _ in range(t):
    n, c, m = map(int, input().split())
    print(solution(n, c, m))
