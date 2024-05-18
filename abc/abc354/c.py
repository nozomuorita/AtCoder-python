from heapq import heapify, heappop, heappush
n = int(input())
ac = []
for i in range(n):
    a, c = map(int, input().split())
    ac.append([-a, c, i])

ans = []
heapify(ac)

while ac:
    a, c, idx = heappop(ac)
    if len(ans)==0:
        ans.append(idx+1)
        cost = c
    else:
        if c<cost:
            ans.append(idx+1)
            cost = c

print(len(ans))
print(*sorted(ans))