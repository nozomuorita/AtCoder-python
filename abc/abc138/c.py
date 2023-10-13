from heapq import heapify, heappop, heappush
n = int(input())
v = list(map(int, input().split()))
v.sort()
heapify(v)

while len(v)!=1:
    v1 = heappop(v)
    v2 = heappop(v)
    t = (v1+v2)/2
    heappush(v, t)
    
print(v[0])