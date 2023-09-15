import sys
sys.setrecursionlimit(10**8)
n, m = map(int, input().split())
cost = [[0]*n for _ in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    cost[a][b] = c
    cost[b][a] = c
    
ans = 0
used = [False]*n

# v: 今見ている頂点
# s: たどった頂点の総距離
def dfs(v, s):
    global ans
    used[v] = True
    if s>ans:
        ans = s
    for i in range(n):
        if not(used[i]) and (cost[v][i]>0):  # iがまだたどっていなくてかつ、つながっているなら
            dfs(i, s+cost[v][i])
    # 関数を終了するときにvをFalse(未訪問)に戻す(次の経路をたどれるようにするため)
    used[v] = False
    
for i in range(n):
    dfs(i, 0)
    
print(ans)