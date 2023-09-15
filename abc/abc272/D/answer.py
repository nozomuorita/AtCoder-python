# 解説AC
from collections import deque

n, m = map(int, input().split())

# (i, j)からm**0.5まで移動できる差分dx, dyを列挙
# dx, dyは、-m**0.5 <= dx, dy <= m**0.5を満たすため、この区間でdx, dyを探す
route_m = int(m ** 0.5) + 1
dxdy = [] # 距離が m**0.5 となるための差分を管理
for i in range(-route_m, route_m):
    for j in range(-route_m, route_m):
        # i**2 + j**2 = m ならば、i と j は距離が m**0.5 となる差分であるため追加
        if i**2 + j**2 == m:
            dxdy.append((i, j))

# 答えを管理する n*n のansを定義
# 初めは、すべて-1で初期化する
ans = [[-1]*n for _ in range(n)]
# (0, 0)は0回で移動できる(最初にいる)ため、0とする
ans[0][0] = 0

q = deque()
# 初期位置をキューに追加
q.append((0, 0))

while q:
    x, y = q.popleft()

    # 事前計算した m**0.5 の距離となる差分をひとつずつ見る
    for dx, dy in dxdy:
        # 移動後が n*n の範囲内であり、かつ、未訪問ならばキューに追加
        if (0 <= x+dx <= n-1) and (0 <= y+dy <= n-1):
            if ans[x+dx][y+dy] == -1:
                ans[x+dx][y+dy] = ans[x][y] + 1
                q.append((x+dx, y+dy))

# 出力
for i in ans:
    print(*i)

