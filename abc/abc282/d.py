import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    u, v = map(lambda x: x-1, map(int, input().split()))
    g[u].append(v)
    g[v].append(u)

#n個の頂点の色を初期化。-1:未着色、0:黒、1:白
colors = [-1 for i in range(n)]
visited = [False]*n

#頂点vをcolor(1 or -1)で塗り、再帰的に矛盾がないか調べる。矛盾があればFalse
def dfs(v,color):
    #今いる点を着色
    colors[v] = color
    visited[v] = True
    cnt[color] += 1
    #今の頂点から行けるところをチェック
    for to in g[v]:
        #同じ色が隣接してしまったらFalse
        if colors[to] == color:
            return exit(print(0))
        #未着色の頂点があったら反転した色を指定し、再帰的に調べる
        if colors[to] == -1 and not dfs(to, int(not(color))):
            return exit(print(0))
    #調べ終わったら矛盾がないのでTrue
    return colors

#2部グラフならTrue, そうでなければFalse
def is_bipartite():
    return dfs(0,1) # 頂点0を黒(1)で塗ってDFS開始

ans = n*(n-1)//2 - m
for i in range(n):
    if visited[i]: continue
    cnt = [0, 0]
    dfs(i, 0)
    ans -= (cnt[0]*(cnt[0]-1)//2) + (cnt[1]*(cnt[1]-1)//2)

print(ans)