"""
・操作1をA回、操作2をB回として、操作1の回数Aを全探索
・上のように考えると、移動後の座標は(A+2B, 2A+B)となる
・(A+2B, 2A+B)=(X, Y)となるようなA, Bを考える。
・A回操作1をしたとすると、2B=X-Aとなる、これを2で割ったあまりが0でないなら、操作2を整数回行うことができないので成立しない
・2で割った余りが0なら操作2はB=(X-A)/2回行われた可能性がある。
・2A+B=Yが成立するなら、操作1をA回、操作2をB回したとしてその操作順の組み合わせを計算
・これはA+Bかいの操作から、操作1をするA回の場所を選択する通りなので(A+B)C(A)となる。
・これを高速にmodで計算する
"""
x, y = map(int, input().split())
mod = 10**9+7

#  nCrのmod高速計算
def combination(n, r, mod):
    r = min(r, n - r)
    numer = denom = 1
    for i in range(1, r + 1):
        numer = numer * (n - i + 1) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod - 2, mod) % mod

ans = 0

for a in range(x + 1):
    b = x - a
    if b % 2 == 1:
        continue
    b //= 2
    if 2 * a + b == y:
        ans = combination(a + b, a, mod)
        break

print(ans)