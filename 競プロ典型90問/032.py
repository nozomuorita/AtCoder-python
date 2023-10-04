"""
・DFSで、走る順番を探索して最小タイムとなるものを求める
"""

import sys
sys.setrecursionlimit(100000000)

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
xy = set()
for i in range(m):
    x, y = map(int, input().split())
    mn = min(x, y)
    mx = max(x, y)
    xy.add((mn, mx))
        
# i番目の選手がk区を走る。k区を走り終えるまでのタイムはtである
def dfs(i, k, t):
    global ans
    
    ran[i] = True   # i番目の選手は走ったのでTrueとする
    
    #  もし、全区間走り終えたならansを更新
    if k==(n-1):
        ans = min(ans, t)
        return
    
    # 次に走る人を決める
    for j in range(n):
        if i==j: continue                                #  同じ人ならcontinue
        if ran[j]: continue                              #  すでに走っているならcontinue
        if (min(i, j)+1, max(i, j)+1) in xy: continue    #  仲が悪い人たちならcontinue
        dfs(j, k+1, t+a[j][k+1])
        ran[j] = False                                   # 戻ってくるときにFalseにする
        
ans = 10**18
for s in range(n):
    ran = [False]*(n+1)
    dfs(s, 0, a[s][0])
    
print(ans) if ans!=10**18 else print(-1)