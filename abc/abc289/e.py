from collections import deque, defaultdict
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    c =  list(map(int, input().split()))
    g = [[] for _ in range(n)]
    for i in range(m):
        u, v = map(lambda x: x-1, map(int, input().split()))
        g[u].append(v)
        g[v].append(u)
        
    #  もし、最初の状態で同じ色なら不可
    if c[0]==c[-1]: print(-1); continue
    
    q = deque()
    q.append((0, n-1))
    dist = {}
    dist[(0, n-1)] = 0
    while q:
        v1, v2 = q.popleft()
        for v3 in g[v1]:
            for v4 in g[v2]:
                if (v3, v4) in dist: continue
                if c[v3]!=c[v4]:
                    dist[(v3, v4)] = dist[(v1, v2)] + 1
                    q.append((v3, v4))
    
    print(dist[(n-1, 0)]) if (n-1, 0) in dist else print(-1)