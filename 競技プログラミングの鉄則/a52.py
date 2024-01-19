"""キュー"""
from collections import deque
Q = int(input())
q = deque()
for _ in range(Q):
    query = list(map(str, input().split()))
    if query[0]=="1":
        q.append(query[1])
    elif query[0]=="2":
        ans = q.popleft()
        print(ans)
        q.appendleft(ans)
    else:
        q.popleft()