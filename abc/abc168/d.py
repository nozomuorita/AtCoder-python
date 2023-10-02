"""
・BFS
"""

from collections import deque
n, m = map(int, input().split())
g = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

visited = [False] * n
ans = [0] * n
q = deque([0])

while q:
    i = q.popleft()

    for j in g[i]:
        if visited[j]: continue

        visited[j] = True
        ans[j] = i
        q.append(j)

if visited[1:].count(True)==(n-1):
    print('Yes')
    for i in range(1, n):
        print(ans[i]+1)
else:
    print('No')    