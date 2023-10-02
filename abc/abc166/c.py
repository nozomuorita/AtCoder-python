n, m = map(int, input().split())
h = list(map(int, input().split()))
g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
    
ans = 0
for i in range(n):
    s = g[i]
    f = True
    for j in s:
        if h[j] >= h[i]:
            f = False
            break
    if f or len(s)==0: ans += 1
        
print(ans)