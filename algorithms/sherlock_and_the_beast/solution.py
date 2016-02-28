# Somewhat obfuscated, but O(1) solution

def solution(n):
    rem = n % 3
    if rem == 0:
        num_fives = n
        num_threes = 0
    elif rem == 1:
        if n >= 10:
            num_fives = n - 10
            num_threes = 10
        else:
            if n % 5 == 0:
                num_fives = 0
                num_threes = n
            else:
                return "-1"
    else: # rem == 2
        if n >= 5:
            num_fives = n - 5
            num_threes = 5
        else:
            if n % 5 == 0:
                num_fives = 0
                num_threes = n
            else:
                return "-1"
    return "".join(map(str, [5]*num_fives + [3]*num_threes))

t = int(input())
for _ in range(t):
    print(solution(int(input())))
