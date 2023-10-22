"""
・UnionFind
・マス(i, j)が'#'ならば、8方向を見る → '#'ならマス(i, j)とつなぐ
・連結成分の個数が答えとなる(連結成分の要素数が1の場合はそのマスが'#'であるときのみOK)
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
    
h, w = map(int, input().split())
s = [input() for _ in range(h)]
ans = 0
a = set()           #  マス(i, j)が"#"であるマスのマス番号を入れる(i*w+j)

uf  =UnionFind(h*w)
for i in range(h):
    for j in range(w):
        if s[i][j]=='#': a.add(i*w+j)       # マス(i, j)が"#"ならば、aに追加(i*w+j)
        if s[i][j]=='.': continue           # マス(i, j)が"."ならば、飛ばす
        p1 = i*w+j                          # マス番号(1次元)に変換
        for d1, d2 in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:   #  8方向を見る
            if 0<=(i+d1)<h and 0<=(j+d2)<w:                      #  グリッドの範囲内なら処理
                if s[i+d1][j+d2]=='.': continue                  #  "."なら飛ばす
                p2 = (i+d1)*w+(j+d2)                            
                uf.union(p1, p2)                                 #  "#"ならばマス(i, j)と接続
                
d  =uf.all_group_members()             #  連結成分を辞書で取得
for key in list(d.keys()):
    if len(d[key])>1: ans += 1         #  もし、連結成分の要素数が1より大きいなら1つのかたまりであるため答えに1を足す
    else:                              #  要素数が1の場合は、その1つのマスが"#"であるかを判定する("."のマスも要素が一つの連結成分となっているため)
        if key in a: ans += 1
    
print(ans)