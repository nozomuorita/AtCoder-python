from collections import defaultdict

n, k, p = map(int, input().split())
c, a = [], []
for i in range(n):
    tmp = list(map(int, input().split()))
    c.append(tmp[0])
    a.append(tmp[1:])

inf = float('inf')

# dp[i][j]: i番目の開発案まで考えて、各パラメータをjとしたときの最小コスト(不可の時はinf)
# ここでjはタプルであり、各パラメータの値を表す → j=(0, 0, 0)のとき、パラメータ1=0、パラメータ1=0、パラメータ2=0である場合を表す
dp = [defaultdict(lambda: inf) for _ in range(n+1)]
# 初期値dp[0][tuple([0]*k)]=dp[0][(0, 0, 0)]=0(サンプル1の場合)であり、0個目の開発案まで考えて各パラメータ(3つ)がすべて0
# である場合の最小コストを表している → この場合、最小コストは0なので0を初期値として入れる
dp[0][tuple([0] * k)] = 0

# n個の開発案を実行するかしないかループを回す(1~(n-1))
for i in range(1, n+1):
    for j in list(dp[i-1].keys()):
        # i個目の開発案を実行しない
        dp[i][j] = min(dp[i-1][j], dp[i][j])

        # i個目の開発案を実行する
        t = [min(p, j[k]+a[i-1][k]) for k in range(k)]
        t = tuple(t)
        dp[i][t] = min(dp[i][t], dp[i-1][j]+c[i-1])
        
if dp[-1][tuple([p]*k)]==inf:
    print(-1)
else:
    print(dp[-1][tuple([p]*k)])


# for i in range(1, N + 1):
#     for j in dp[i - 1].keys():
#         # i個目の開発案を実行しない場合
#         dp[i][j] = min(dp[i][j], dp[i - 1][j])

#         # i個目の開発案を実行する場合
#         tup = tuple([min(P, j[k] + up[i - 1][k]) for k in range(K)])
#         dp[i][tup] = min(dp[i][tup], dp[i - 1][j] + cost[i - 1])

# print(-1 if tuple([P] * K) not in dp[N].keys() else dp[N][tuple([P] * K)])