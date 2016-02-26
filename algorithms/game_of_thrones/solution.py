def solution(s):
    found_odd = False
    for c in set(s):
        count = s.count(c)
        if count % 2 == 1:
            if found_odd:
                return "NO"
            else:
                found_odd = True
    return "YES"

s = input()
print(solution(s))
