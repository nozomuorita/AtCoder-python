"""
・二分探索
・各イチゴを属している区画の左下(隅)に寄せて同じ区画に属しているイチゴを同一座標にまとめる
・すると、同一座標にあるイチゴは同じ区画にあるものなので、辞書でカウントして最大数を求める
・隅に寄せるときは二分探索で求める
・最小値については一つもイチゴが乗っていない区画があるか判定する必要がある->全区画数は(A+1)*(B+1)なので、辞書にあるkeyの数と比較し求める
"""

from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict
w, h = map(int, input().split())
n = int(input())
pq = [list(map(int, input().split())) for _ in range(n)]
A = int(input())
a = list(map(int, input().split()))
B = int(input())
b = list(map(int, input().split()))

a.insert(0, 0)
a.append(w)
b.insert(0, 0)
b.append(h)

d = defaultdict(int)

for i in range(n):
    st = pq[i]
    idx1 = bisect_left(a, st[0])
    idx2 = bisect_left(b, st[1])
    
    d[(idx1, idx2)] += 1
    
mn, mx = 10**18, -1
for key in list(d.keys()):
    mn = min(mn, d[key])
    mx = max(mx, d[key])

if len(list(d.keys()))<((A+1)*(B+1)):  # 全区画数よりキーの数が小さいなら一つも載っていないイチゴがある
    mn = 0
    
print(mn, mx)