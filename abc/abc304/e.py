"""
・つなごうとしている頂点の連結成分(renketsu1, renketsu2)==つないではいけない頂点の連結成分(renketsu3, renketsu4)ならNoとなる
・ゆえに、以下のものを求める
・各頂点の連結成分 -> 辞書(key: 頂点、value: 連結成分num)を用意し、各頂点が所属する連結成分を求めておく
・つないではいけない連結成分 -> 辞書(key: ダメな連結成分num(タプル)、value: bool)を用意し、つないではいけない連結成分を求めておく
・つなごうとしている頂点の連接成分がつないではいけない連結成分であるのかを判定し、出力
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
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    uf.union(u, v)

f = True                                 #  初期状態が良いグラフであるかどうか
k = int(input())
xy = []
for i in range(k):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    xy.append((x, y))
    if uf.same(x, y):                    #  xとyが同じ連結成分なら、パスが存在するのですでに良いグラフではない
        f = False
        break

#  初期状態が良いグラフでないならすべてNoである(どの頂点同士をつないでも良いグラフでないことに変わりはない)
if not f:
    # 入力は不要だが受け取らなければいけないので受け取っておく
    q = int(input())
    pq = [list(map(int, input().split())) for _ in range(q)]
    for i in range(q):
        print('No')
    exit()

# 連結成分を表す辞書(各頂点が属する連結成分を管理、値は親ノードとする、親ノードが同じなら同じ連結成分である)
d_renketsu = defaultdict(lambda: 0)
num = 1
for i in range(n):
    d_renketsu[i] = uf.find(i)
        
# つないではいけない連結成分
d_bad = defaultdict(lambda: False)
for i in range(len(xy)):
    x, y = xy[i][0], xy[i][1]
    renketsu1 = d_renketsu[x]       #  つないではいけない頂点の連結成分(親ノード)を取得
    renketsu2 = d_renketsu[y]       #  上に同様
    d_bad[(min(renketsu1, renketsu2), max(renketsu1, renketsu2))] = True    # keyはタプルでつないではいけない連結成分とする(小さいほうが先に来るように)
    
q = int(input())
for i in range(q):
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    p_renketsu = d_renketsu[p]                 # つなごうとしている頂点の連結成分num
    q_renketsu = d_renketsu[q]                 # 上に同様
    renketsu1 = min(p_renketsu, q_renketsu)    # key指定するときに小さいほうが先に来るようにする
    renketsu2 = max(p_renketsu, q_renketsu)
    if d_bad[(renketsu1, renketsu2)]:          # つないではいけない連結成分ならNo
        print('No')
    else:
        print('Yes')