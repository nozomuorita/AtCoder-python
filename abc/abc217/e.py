from heapq import heapify, heappush, heappop
from collections import deque
Q = int(input())

q = deque()
hq = []
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0]==1:
        q.append(query[1])
    elif query[0]==2:
        if hq: print(heappop(hq))
        else: print(q.popleft())
    else:
        while q:
            v = q.popleft()
            heappush(hq, v)
