"""
・UnionFind
・h*wのグリッドを線形変換し(1次元にする)、h*w個の頂点としてUnionFindで接続情報を管理する
・(i, j)マスは線形変換により、i*w+jに置き換えることができる
・UnionFindとは別に、マスが赤色であるかどうかを辞書で管理する(同様に線形変換した値をキーとして、赤ならTrueとする)
・クエリ１：辞書のマス(i, j)(=i*w+j)をTrueにする
・上下左右のマスについて、線形変換を行い、そのマスが赤色ならばUnionFindで結合する
・クエリ２：頂点１と頂点２の親ノードを調べ(uf.find())、同じ親であるならつながっているのでYes(頂点１、頂点２がともに赤色でないならそもそもNo)
・別の方法として、uf,sane(v1, v2)でもok
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
d = defaultdict(lambda: False)
uf = UnionFind(h*w)

Q = int(input())
for i in range(Q):
    q = list(map(int, input().split()))
    if q[0]==1:
        r, c=q[1], q[2]
        r-=1
        c-=1
        t1 = w*r+c          # 線形変換
        d[t1] = True        # 赤色にする(Trueにする)
        
        for i2, j2 in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:    # 上下左右のマスを見る
            if not(0<=i2<h and 0<=j2<w): continue                  # 範囲外なら飛ばす
            t2 = w*i2+j2                                  
            if d[t2]: uf.union(t1, t2)                             # 結合
        
    else:
        ra, ca, rb, cb=q[1]-1, q[2]-1, q[3]-1, q[4]-1
        t3 = w*ra+ca
        t4 = w*rb+cb
        if d[t3]==False or d[t4]==False: print('No')               # どちらも赤色でないならNo
        else:
            if uf.find(t3)==uf.find(t4):                           # 親ノードが同じなら移動によりたどり着くことができる
                print('Yes')
            else:
                print('No')