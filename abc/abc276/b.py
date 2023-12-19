n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
    
for i in range(1, n+1):
    ans = sorted(g[i])
    print(len(ans), *ans)