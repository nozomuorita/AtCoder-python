from collections import deque

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
    
q = deque()
q.append(0)
dist = [-1] * n  # -1: 未訪問
dist[0] = 0

while q:
    num = q.popleft()
    for i in g[num]:
        if dist[i] != -1:
            continue
        dist[i] = dist[num] + 1
        q.append(i)
        
if dist[-1]==2:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')