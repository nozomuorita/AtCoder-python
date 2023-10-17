from collections import defaultdict
n, C = map(int, input().split())
d = defaultdict(int)
for i in range(n):
    a, b, c = map(int, input().split())
    d[a] += c
    d[b+1] -= c
  
keys = sorted(list(d.keys()))  
d2 = defaultdict(int)
d2[keys[0]] = d[keys[0]]
for i in range(1, len(keys)):
    d2[keys[i]] = d2[keys[i-1]] + d[keys[i]]
    
ans = 0
keys2 = list(d2.keys())
for i in range(1, len(keys2)):
    if d2[keys2[i-1]]<C:
        ans += d2[keys2[i-1]] * (keys2[i]-keys2[i-1])
    else:
        ans += C * (keys2[i]-keys2[i-1])
    
print(ans)