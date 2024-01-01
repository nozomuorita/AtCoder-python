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

uf = UnionFind(h*w)
for i in range(h):
    for j in range(w):
        color="black" if s[i][j]=="#" else "white"
        masu1 = i*w+j
        for d1, d2 in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if not(0<=(i+d1)<h and 0<=(j+d2)<w): continue
            if color=="black" and s[i+d1][j+d2]=="#": continue
            if color=="white" and s[i+d1][j+d2]==".": continue
            masu2 = (i+d1)*w+(j+d2)
            if not(uf.same(masu1, masu2)): uf.union(masu1, masu2)

renketsu = uf.all_group_members()
ans = 0
for key in list(renketsu.keys()):
    bw = [0, 0]
    for k in renketsu[key]:
        i, j = k//w, k%w
        if s[i][j]=="#": bw[0]+=1
        else: bw[1]+=1
    
    ans += bw[0]*bw[1]

print(ans)