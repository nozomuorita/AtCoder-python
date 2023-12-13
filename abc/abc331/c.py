from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
a2 = a.copy()
a.sort()

d = defaultdict(int)
for i in a:
    d[i] += 1
    
keys = list(d.keys())
d2 = defaultdict(int)
d2[keys[0]] = keys[0]*d[keys[0]]
for i in range(1, len(keys)):
    d2[keys[i]] = d2[keys[i-1]] + (keys[i]*d[keys[i]])

s = sum(a)
for i in range(n):
    ans = s - d2[a2[i]]
    print(ans)
