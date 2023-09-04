from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

d = defaultdict(int)
for i in range(n):
    d[a[i]] += 1

if len(list(d.keys()))<=k:
    ans = 0
else:
    num = len(list(d.keys()))
    delete_num = num - k
    d2 = sorted(d.items(), key=lambda x:x[1])
    ans = 0
    for i in range(delete_num):
        ans += d2[i][1]

print(ans)