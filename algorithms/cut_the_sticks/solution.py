def solution(arr):
    while arr:
        print(len(arr))
        arr = [e - min(arr) for e in arr if e - min(arr) > 0]

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
solution(arr)
