from collections import defaultdict

n = int(input())
s = [input() for _ in range(n)]

d = defaultdict(int)
for i in range(n):
    d[s[i]] += 1
    
d2 = defaultdict(list)
for i in list(d.keys()):
    d2[d[i]].append(i)
    
mx = max(list(d2.keys()))
ans = d2[mx]
ans.sort()
print(*ans, sep='\n')