from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)

for i in a:
    d[i] += 1

ans = 0
for key in list(d.keys()):
    ans += d[key] // 2

print(ans)