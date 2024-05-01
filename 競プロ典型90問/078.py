from bisect import bisect_left, bisect_right, insort_left, insort_right
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(lambda x:x-1, map(int, input().split()))
    g[a].append(b)
    g[b].append(a)

ans = 0
for i in range(n):
    idx = bisect_left(sorted(g[i]), i)
    if idx==1: ans+=1
print(ans)