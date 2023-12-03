"""
・各連結成分を見て、頂点数(=all_group_membersの値の要素数)と辺の数(=その要素の辺の数の和//2)が等しくないならno
・辺の数はつながっている頂点同士で二重に数えるので最後に//2する。
"""
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
    
n, m = map(int, input().split())
uf = UnionFind(n)
g = [[] for _ in range(n)]
for i in range(m):
    u, v = map(lambda x: x-1, map(int, input().split()))
    g[u].append(v)
    g[v].append(u)
    uf.union(u, v)

d = uf.all_group_members()
for key in list(d.keys()):
    v_num = len(d[key])
    h_num = 0
    for i in d[key]:
        h_num += len(g[i])
    if v_num!=h_num//2: exit(print('No'))
    
print('Yes')