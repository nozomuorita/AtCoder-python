import sys
sys.setrecursionlimit(100000000)

n = int(input())
d = [[0]*(i+1) + list(map(int, input().split())) for i in range(n-1)]
ans = 0

used = [False]*n

def dfs(lst, score):
    global ans
    if all(lst):
        ans = max(ans, score)
        return 0
        
    v = lst.index(False)
    lst[v] = True
    for v2 in range(v+1, n):
        if lst[v2]: continue
        score += d[v][v2]
        lst[v2] = True
        dfs(lst, score)
        lst[v2] = False
        score -= d[v][v2]
    lst[v] = False
    
if n%2==0: dfs(used, 0)
else:
    for i in range(n):
        used[i] = True
        dfs(used, 0)
        used[i] = False
    
print(ans)