"""
・誤差をなくす
・式変形することで、小数演算をなくす
・blog(c) = log(c**b)であることから真数を比較することで判定できる
"""

a, b, c = map(int, input().split())
if a < c**b:
    print('Yes')
else:
    print('No')