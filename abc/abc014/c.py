from collections import defaultdict
n = int(input())
d = defaultdict(int)

for i in range(n):
    a, b = map(int, input().split())
    d[a] += 1
    d[b+1] -= 1

keys = sorted(list(d.keys()))
d2 = defaultdict(int)
d2[keys[0]] = d[keys[0]]
for i in range(1, len(keys)):
    d2[keys[i]] = d2[keys[i-1]] + d[keys[i]]

ans = max(list(d2.values()))
print(ans)