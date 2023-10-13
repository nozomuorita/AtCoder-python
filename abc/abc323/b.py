from collections import defaultdict

n = int(input())
s = [input() for _ in range(n)]

d = defaultdict(list)
for i in range(n):
    t = s[i].count('o')
    d[t].append(i+1)
    
keys = sorted(list(d.keys()), reverse=True)
ans = []
for key in keys:
    tmp = d[key]
    tmp.sort()
    ans += tmp

print(*ans)