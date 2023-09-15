import math
from itertools import combinations, permutations, product, accumulate, groupby, chain

c = [list(map(int, input().split())) for _ in range(3)]
d = []
for i in range(3):
    for j in range(3):
        d.append((i, j))

ans = 0
g = 0

# 数字をもらう順番を列挙
# 全探索する
l = list(range(0, 9))
s = list(permutations(l, 9))
for i in s:
    # 縦の列についてがっかりするか判定
    f = True # がっかりしたか判定(Falseならがっかりする順番である)
    if f:
        for j in range(3):
            if f:
                n1 = i.index(j*3+0)
                n2 = i.index(j*3+1)
                n3 = i.index(j*3+2)
                tmp = sorted([(n1, j*3+0), (n2, j*3+1), (n3, j*3+2)])
                c1 = c[d[tmp[0][1]][0]][d[tmp[0][1]][1]]
                c2 = c[d[tmp[1][1]][0]][d[tmp[1][1]][1]]
                c3 = c[d[tmp[2][1]][0]][d[tmp[2][1]][1]]
                if (c1==c2) and (c1!= c3):
                    g += 1
                    f = False
    # 横の列についてがっかりするか判定
    # すでにがっかりしているなら見なくてよい
    if f:
        for j in range(3):
            if f:
                n1 = i.index(j)
                n2 = i.index(j+3)
                n3 = i.index(j+6)
                tmp = sorted([(n1, j), (n2, j+3), (n3, j+6)])
                c1 = c[d[tmp[0][1]][0]][d[tmp[0][1]][1]]
                c2 = c[d[tmp[1][1]][0]][d[tmp[1][1]][1]]
                c3 = c[d[tmp[2][1]][0]][d[tmp[2][1]][1]]
                if (c1==c2) and (c1!= c3):
                    g += 1
                    f = False
    # ななめについて判定
    if f:
        n1 = i.index(0)
        n2 = i.index(4)
        n3 = i.index(8)
        tmp = sorted([(n1, 0), (n2, 4), (n3, 8)])
        c1 = c[d[tmp[0][1]][0]][d[tmp[0][1]][1]]
        c2 = c[d[tmp[1][1]][0]][d[tmp[1][1]][1]]
        c3 = c[d[tmp[2][1]][0]][d[tmp[2][1]][1]]
        if (c1==c2) and (c1!= c3):
            g += 1
            f = False
    if f:
        n1 = i.index(2)
        n2 = i.index(4)
        n3 = i.index(6)
        tmp = sorted([(n1, 2), (n2, 4), (n3, 6)])
        c1 = c[d[tmp[0][1]][0]][d[tmp[0][1]][1]]
        c2 = c[d[tmp[1][1]][0]][d[tmp[1][1]][1]]
        c3 = c[d[tmp[2][1]][0]][d[tmp[2][1]][1]]
        if (c1==c2) and (c1!= c3):
            g += 1
            f = False
                
#  数字を教えてもらう順番は全部で9!
ss = math.factorial(9)
ans = (ss-g) / ss
print(ans)