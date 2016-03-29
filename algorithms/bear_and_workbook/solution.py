n, k = map(int, input().split())
t = list(map(int, input().split()))
page_no = 0
count = 0
for num_problems in t:
    bpn = 0
    while num_problems > 0:
        epn = bpn + (k if num_problems > k else num_problems) - 1
        if page_no >= bpn and page_no <= epn:
            count += 1
        num_problems -= (epn - bpn) + 1
        page_no += 1
        bpn = epn + 1
print(count)
