from sortedcontainers import SortedList
Q = int(input())
sl = SortedList()
for _ in range(Q):
    query = list(map(int, input().split()))
    x = query[1]
    if query[0]==1:
        sl.add(x)
    elif query[0]==2:
        sl.remove(x)
    else:
        idx = sl.bisect_left(x)
        if idx==len(sl): print(-1)
        else: print(sl[idx])