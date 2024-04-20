from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
ans = []
d = defaultdict(int)
d2 = defaultdict(int)
for i in range(n):
    d[a[i]] = i+1
    d2[i+1] = a[i]

for i in range(1, n+1):
    if d[i]!=i:
        ans.append((min(i, d[i]), max(i, d[i])))
        tmp = d[i]
        tmp2 = d2[i]
        d[i], d[tmp2] = d[tmp2], d[i]
        d2[tmp], d2[i] = d2[i], d2[tmp]
        
print(len(ans))
for i in ans:
    print(*i)