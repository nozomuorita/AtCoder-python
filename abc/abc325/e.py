"""
・ダイクストラ法
・都市1から都市iまで社用車で行くときの最小コストをダイクストラ法で計算
・都市iから都市nまで電車で行くときの最小コストをダイクストラ法で計算
・都市iまで社用車で行って、都市iから都市nまで電車で行くときの最小コストを上で求めたものから計算する
・都市iから都市nまで電車で行くときの最小コストは「都市nを始点として都市iまで行くとき」と置き換えれば、1回のダイクストラで計算可能
"""

from heapq import heapify, heappop, heappush
n, a, b, c = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(n)]

#  dist1[i]: 社用車のみを使って都市1から都市iに行く最小コスト
dist1 = [-1]*n
dist1[0] = 0
visited1 = [False]*n
q1 = []
heappush(q1, (0, 0))      #  (距離, 頂点)

while q1:
    i, j = heappop(q1)    #  i: 距離、j: 頂点
    
    if visited1[j]: continue
    visited1[j] = True
    
    for k in range(n):
        if j==k: continue
        x = i + (d[j][k]*a)
        if dist1[k]==-1 or (dist1[k]>x):
            dist1[k] = x
            heappush(q1, (x, k))
            
#  dist2[i]: 都市iから電車のみを使って都市Nに行く最小コスト
#  これは、都市Nからスタートして都市iまで行くのにかかるコストと等しい
dist2 = [-1]*n
dist2[-1] = 0
visited2 = [False]*n
q2 = []
heappush(q2, (0, n-1))

while q2:
    i, j = heappop(q2)
    if visited2[j]: continue
    visited2[j] = True
    
    for k in range(n):
        if j==k: continue
        x = i + (d[j][k]*b+c)
        if dist2[k]==-1 or dist2[k]>x:
            dist2[k] = x
            heappush(q2, (x, k))
            
ans = float('inf')
#  都市iまで、社用車を使うとする
for i in range(n):
    t = dist1[i] + dist2[i]
    ans = min(ans, t)
    
print(ans)