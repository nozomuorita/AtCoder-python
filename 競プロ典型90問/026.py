"""
・bfs、dfs(方針あってた)
・頂点0からbfsしていき、頂点0からの距離を求める
・頂点0からの距離が偶数であるもの(頂点0を含む)と奇数であるものを求める
・距離が偶数であるもの、奇数であるもののどちらかが(n//2)以上あるので、多いほうから(n//2)個選んで出力する
・二部グラフについて: 公式解説X参照
"""

from collections import deque
n = int(input())
g = [[] for _ in range(n)]

for i in range(n-1):
    a, b = map(lambda x: x-1, map(int, input().split()))
    g[a].append(b)
    g[b].append(a)
    
q = deque()
q.append(0)
dist = [-1]*n
dist[0] = 0
ans = [1]       # 頂点0からの距離が偶数であるもの(1-index)
ans2 = []       # 頂点0からの距離が奇数であるもの(1-index)

while q:
    v = q.popleft()
    for v2 in g[v]:
        if dist[v2]!=-1: continue
        dist[v2] = dist[v]+1
        if dist[v2]%2==0: ans.append(v2+1)      # 距離が偶数
        else: ans2.append(v2+1)                 # 距離が奇数
        q.append(v2)
        
# 距離が偶数のもの、奇数のもののうち多いほうからn//2個出力
if len(ans)>=len(ans2):
    print(*ans[:(n//2)])
else:
    print(*ans2[:(n//2)])