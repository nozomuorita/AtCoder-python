from collections import defaultdict
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    # 要素xが属するグループの根(親)を返す
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    # 要素xと要素yを結合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    # 要素xが属するグループの要素数を返す
    def size(self, x):
        return -self.parents[self.find(x)]
    # 要素xと要素yが同じグループに属するかを返す
    def same(self, x, y):
        return self.find(x) == self.find(y)
    # 要素xが属するグループのメンバーをリストで返す
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    # 全ての根の要素をリストで返す
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    # グループの数(連結成分数)を返す
    def group_count(self):
        return len(self.roots())
    # 辞書型を返す
    # キーは，グループのルート要素
    # 値は，そのルート要素に含まれるメンバーのリスト
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members
    # ルート要素: [そのグループに含まれる要素のリスト]を文字列で返す
    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
    
n = int(input())
sx, sy, tx, ty = map(int, input().split())
xyr = [list(map(int, input().split())) for _ in range(n)]

sp, tp = [], []
for i in range(n):
    x, y, r = map(int, xyr[i])
    f1=True if ((sx-x)**2)+((sy-y)**2)==r**2 else False
    f2=True if ((tx-x)**2)+((ty-y)**2)==r**2 else False
    if f1 and f2: exit(print('Yes'))
    elif f1: sp.append(i)
    elif f2: tp.append(i)

uf = UnionFind(n)

for i in range(n):
    for j in range(i+1, n):
        # 交わる条件は中心間の距離が和以下
        x1, y1, r1 = map(int, xyr[i])
        x2, y2, r2 = map(int, xyr[j])
        d = ((x1-x2)**2 + (y1-y2)**2)   # ルートをつけると誤差でWAになる
        if abs(r1-r2)**2<=d<=(r1+r2)**2:
            uf.union(i, j)

for i in sp:
    for j in tp:
        if uf.same(i, j): exit(print('Yes'))

print('No')