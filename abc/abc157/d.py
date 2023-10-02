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

n, m, k = map(int, input().split())
uf = UnionFind(n)
g1 = [[] for _ in range(n)]   #  直接交友関係にある(隣接リスト)
g2 = [[] for _ in range(n)]   #  ブロック関係にある(隣接リスト)

# 直接交友関係を隣接リストに加える
# UnionFindで結合
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g1[a].append(b)
    g1[b].append(a)
    uf.union(a, b)
    
# ブロック関係を隣接リストに加える
for i in range(k):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    g2[c].append(d)
    g2[d].append(c)
    
ans = []
# 各人の友人候補を計算
for i in range(n):
    s = uf.size(i)          #  人iの連結成分数が候補となる(uf.size)
    s -= 1                  #  連結成分数から自分自身を引く
    s -= len(g1[i])         #  直接の友達関係(g1[i])を引く
    for j in g2[i]:         #  人iのブロック関係を一人ずつ見て、同じ連結成分なら引く
        if uf.same(i, j):
            s -= 1
    ans.append(s)
    
print(*ans)