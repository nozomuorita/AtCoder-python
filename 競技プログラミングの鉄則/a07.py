from collections import defaultdict
d = int(input())
n = int(input())
p = defaultdict(int)

for i in range(n):
    l, r = map(int, input().split())
    p[l] += 1
    p[r+1] -= 1

keys = sorted(p.keys())
p2 = defaultdict(int)
p2[keys[0]] = p[keys[0]]
for i in range(1, len(keys)):
    p2[keys[i]] = p2[keys[i-1]] + p[keys[i]]
p2[0] = 0

keys = list(p2.keys())
idx = 0
score = 0
for i in range(1, d+1):
    if i==keys[idx]:
        score = p2[keys[idx]]
        idx += 1
    print(score)