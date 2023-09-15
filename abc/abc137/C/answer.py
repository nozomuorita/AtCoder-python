from collections import defaultdict

n = int(input())
s = []
for i in range(n):
    _ = sorted(list(input()))
    _ = ''.join(_)
    s.append(_)

d = defaultdict(int)
for i in range(n):
    d[s[i]] += 1
    
ans = 0
for key in d.keys():
    ans += (d[key]*(d[key]-1)) // 2
    
print(ans)