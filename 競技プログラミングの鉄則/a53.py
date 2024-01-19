from heapq import heapify, heappop, heappush
Q = int(input())
q = []
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0]==1:
        heappush(q, query[1])
    elif query[0]==2:
        ans = heappop(q)
        print(ans)
        heappush(q, ans)
    else:
        heappop(q)