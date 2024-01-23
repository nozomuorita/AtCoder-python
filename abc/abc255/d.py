"""
・xより大きいものと小さいものに分ける
・入力例1の場合
・a=[2, 5, 5, 6, 11]
・5より小さいものは、2の一つ
・5*1 - 2が小さいほうの答え
・5より大きいものは6, 11の二つ
・(6+11) - (5*2)が大きいほうの答え
"""
from bisect import bisect_left, bisect_right, insort_left, insort_right
n, q = map(int, input().split())
a = sorted(list(map(int, input().split())))
a_cum = [0]
for i in range(n):
    a_cum.append(a_cum[-1]+a[i])

for _ in range(q):
    x = int(input())
    idx1 = bisect_left(a, x)
    idx2 = bisect_right(a, x)

    score = (x*idx1) - a_cum[idx1]
    score += (a_cum[-1]-a_cum[idx2]) - (x*(n-idx2))

    print(score)