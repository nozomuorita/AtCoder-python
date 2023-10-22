from heapq import heappush, heappop, heapify

n = int(input())
td = []
for i in range(n):
    t, d = map(int, input().split())
    td.append([t, t+d])

td.append([10**20, 10**20+1])
td.sort()

h = []
ans = 0
now = 0
for t, d in td:
    while h and now<t:
        p = heappop(h)
        if now<=p:
            ans += 1
            now += 1
    heappush(h, d)
    now = t
    
print(ans)