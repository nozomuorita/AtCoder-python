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
uf = UnionFind(10**7+5)
black = [False]*(10**7+5)
d = [[-1, -1], [-1, 0], [0, -1], [0, 1], [1, 0], [1, 1]]
for i in range(n):
    x, y = map(int, input().split())
    x+=1001; y+=1001
    now = (2*(10**3))*x + y
    
    for d1, d2 in d:
        if black[(2*(10**3))*(x+d1)+(y+d2)]:
            uf.union(now, (2*(10**3))*(x+d1)+(y+d2))
    
    black[now] = True

ans = 0
root = uf.roots()
for r in root:
    if black[r]: ans+=1

print(ans)

# 別解
# dxdy = ((-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1))

# N = int(input())
# P = [tuple(map(int, input().split())) for _ in range(N)]

# uf = UnionFind(N)
# for i in range(N):
#     x1, y1 = P[i]
#     for j in range(i+1, N):
#         x2, y2 = P[j]
        
#         if any(x1+dx == x2 and y1+dy == y2 for dx, dy in dxdy):
#             uf.union(i, j)

# print(uf.group_count())