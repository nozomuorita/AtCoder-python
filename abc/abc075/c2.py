"""DFS"""
import sys
sys.setrecursionlimit(100000000)

n, m = map(int, input().split())
g = [[] for _ in range(n)]
ab = []
for i in range(m):
    a, b = map(lambda x:x-1, map(int, input().split()))
    g[a].append(b)
    g[b].append(a)
    ab.append([a, b])
    
    
def dfs(i):
    global d
    used[i] = True
    
    for v in g[i]:
        if used[v]: continue
        if [min(i, v), max(i, v)]==ab[d]: continue   # d番目の辺なら再帰しない
        dfs(v)
        
ans = 0
for d in range(m):                   # d番目の辺を無視
    used = [False]*n
    dfs(0)
    
    if used.count(True)!=n: ans+=1   #  Trueがn個でないなら連結でない

print(ans)