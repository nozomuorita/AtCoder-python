"""
・各地点から地点へ行く最短パス数と最大値を事前計算する
・dist[i][j]: i番目の地点からj番目の地点へ行くときの最短パス数と最大値
"""
from collections import deque
n = int(input())
a = list(map(int, input().split()))
g = [[] for _ in range(n)]                           #  隣接リスト
for i in range(n):
    s = input()
    for j in range(n):
        if s[j]=="Y": g[i].append(j)

dist = []
for i in range(n):                                  #  i番目の地点を始点としたときの各地点までの値を計算
    d = [[-1, -1] for _ in range(n)]                #  d[j]: j番目の地点まで行くときの[パス数, 最大値]
    d[i] = [0, a[i]]                                #  i番目からi番目はパス数0、値はその点の土産の価値
    
    q = deque()
    q.append((0, i, a[i]))                          #  キューの要素は(最短パス数, 今見ている頂点, 最大価値)
    while q:
        t = q.popleft()
        path_n, v, score = t[0], t[1], t[2]
        
        for v2 in g[v]:                            #  vとつながっている点をループで
            if d[v2][0]==-1:                       #  v2が未訪問なら
                d2 = d[v][0] + 1                   #  v2までのパス数はvまでのパス数+1
                score2 = d[v][1] + a[v2]           #  価値はvまでの価値に頂点v2の価値を足したもの
                d[v2] = [d2, score2]               #  未訪問なので、これが最大価値となり、dを更新
                q.append((d2, v2, score2))         #  キューに入れる
            else:
                if d[v][0]+1>d[v2][0]: continue    #  v2まで行くパス数が今までの最小パス数より大きいならダメなのでcontinue
                d2 = d[v][0]+1                     #  v2までのパス数
                score2 = d[v][1] + a[v2]           #  価値
                if score2>d[v2][1]:                #  もし、最大価値が更新されるなら
                    d[v2] = [d2, score2]           #  dを書き換え
                    q.append((d2, v2, score2))     #  キューに追加
    
    dist.append(d)                                 #  i番目を始点とするものをすべて計算したらdistに追加

q = int(input())
for _ in range(q):
    u, v = map(lambda x: x-1, map(int, input().split()))
    if dist[u][v][0]==-1: print("Impossible")      #  -1なら到達不可
    else: print(dist[u][v][0], dist[u][v][1])