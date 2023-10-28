"""
・1次元多項式の計算
・pythonはnumpyのpoly1dを使うと高速に計算できる(リストとかだと遅い)
"""

import numpy as np

n, m = map(int, input().split())
a = list(reversed(list(map(int, input().split()))))
c = list(reversed(list(map(int, input().split()))))

ap = np.poly1d(a)
cp = np.poly1d(c)

bp = cp / ap    # 計算結果はタプル(商、余り)で返る
ans = list(reversed(bp[0].coef))
ans = map(lambda x: int(x), ans)
print(*ans)