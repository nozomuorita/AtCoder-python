from collections import defaultdict, deque
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    u, v = map(lambda x: x-1, map(int, input().split()))
    g[u].append(v)
    g[v].append(u)

k = int(input())
dic = defaultdict(lambda: -1)
pd = []
for i in range(k):
    p, d = map(int, input().split())
    pd.append([p-1, d])
    dic[p-1] = d
    
color = [1]*n   # (0: white, 1: black)
dists = []

for i in range(n):
    q = deque([i])
    dist = [-1]*n
    dist[i] = 0
    
    while q:
        v = q.popleft()
        
        for v2 in g[v]:
            if dist[v2]!=-1: continue
            dist[v2] = dist[v] + 1
            q.append(v2)
    
    if dic[i]!=-1:
        for j in range(n):
            if dist[j]==-1: continue
            if dist[j]<dic[i]: color[j]=0
    
    dists.append(dist)

ans = ""
black = []
for i in range(n):
    ans+=str(color[i])
    if color[i]==1: black.append(i)

for i in range(k):
    p, d = pd[i][0], pd[i][1]
    mn = 10**18
    for j in black:
        if dists[p][j]==-1: continue
        mn = min(mn, dists[p][j])
    if mn!=d: exit(print('No'))

if ans.count("1")==0: print('No')
else:
    print('Yes')
    print(ans)