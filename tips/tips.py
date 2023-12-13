"""
・floatが整数であるか判定(is_integer())
・平方数の判定に使用(ルートをとったものが整数であるか)
"""
print("\nfloat型の値が整数であるかの判定", "="*49)
n1 = 1.00
n2 = 1.23
print(f'n1({n1}): {n1.is_integer()}')
print(f'n2({n2}): {n2.is_integer()}')


"""
・defaultdictを値でソート
・結果はリスト(各要素はタプル)となる
"""
print("\n・defaultdictを値でソート", "="*55)
from collections import defaultdict
d = defaultdict(int)
d['a'] = 2
d['b'] = 1
d['c'] = 8
d2 = sorted(d.items(), key=lambda x:x[1])
print(f'd2: {d2}')


"""
・分数計算(Fractionライブラリ)
"""
print("\n・分数計算", "="*70)
from fractions import Fraction

# Fraction(a, b)でa/bを表す
print(f'3分の1はFraction(1, 3): {Fraction(1, 3)}')

# 分数の加減乗除も可能
ans = Fraction(1, 2) + Fraction(1, 3)
print(f'和: {ans}')
ans = Fraction(1, 2) - Fraction(1, 3)
print(f'差: {ans}')
ans = Fraction(1, 2) * Fraction(1, 3)
print(f'積: {ans}')
ans = Fraction(1, 2) / Fraction(1, 3)
print(f'商: {ans}')

# 分母と分子の取り出し(分母: denominator, 分子: numerator)
ans = Fraction(1, 3)
print(f'分母: {ans.denominator}')
print(f'分子: {ans.numerator}')


"""
・確率mod
"""
print("\n・確率mod", "="*70)
mod = 998244353

def p_mod(bunsi, bunbo, mod):
    denominator = pow(bunbo, mod - 2, mod)
    print(bunsi * denominator % mod)    
p_mod(7, 27, mod)


"""
・二次元配列の回転(deg: 0=回転なし、1=90°左回転、2=90°右回転、3=180°回転)
"""
def rotate(p, deg):
    # 回転なしならそのまま返す
    if deg==0:
        return p
    # 90°左回転
    elif deg==1:
        #  90°左回転は、転置してから上下逆にする
        tp = []
        transposed = list(zip(*p))
        for i in transposed[::-1]:
            tp.append(list(i))
        return tp
    # 90°右回転
    elif deg==2:
        # 90°右回転は、上下逆にしてから転置する
        tp = []
        for i in p[::-1]:
            tp.append(i)
        tp = list(zip(*tp))
        tp2 = [list(i) for i in tp]
        return tp2
    # 180°回転
    elif deg==3:
        #  180°回転なら、左右逆にしてから上下逆
        tp = []
        for i in p[::-1]:
            tp.append(i[::-1])
        return tp                
