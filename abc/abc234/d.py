from heapq import heapify, heappop, heappush

n, k = map(int, input().split())
p = list(map(int, input().split()))

p2 = sorted(p[:k])
print(p2[0])
heapify(p2)

for i in range(k, n):
    mn = heappop(p2)
    if p[i] <= mn:
        print(mn)
        heappush(p2, mn)
    else:
        heappush(p2, p[i])
        mn = heappop(p2)
        print(mn)
        heappush(p2, mn)