from heapq import heapify, heappop, heappush
from collections import defaultdict
n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = sum(a)

q = list(set(a))
heapify(q)
d = defaultdict(int)
for i in a: d[i] += 1

for i in range(m):
    b, c = map(int, input().split())
    cnt = 0
    while cnt<b:
        v = heappop(q)
        if v>c:
            heappush(q, v)
            break
        if d[v]>0:
            num = min(b-cnt, d[v])
            cnt += num
            ans += num*(c-v)
            d[v] -= num
            d[c] += num
            if d[v]>0: heappush(q, v)
            if d[c]>0: heappush(q, c)

print(ans)