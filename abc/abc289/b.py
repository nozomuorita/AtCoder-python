import sys
sys.setrecursionlimit(100000000)

n, m = map(int, input().split())
a = list(map(int, input().split()))
g = [[] for _ in range(n)]
for i in a:
    g[i-1].append(i)
    g[i].append(i-1)

def dfs(i):
    for v in g[i]:
        if v+1 in c: continue
        c.append(v+1)
        dfs(v)
        
ans = []
for i in range(n):
    if i+1 in ans: continue
    c = [i+1]
    dfs(i)
    
    c.sort(reverse=True)
    ans += c
    
print(*ans)