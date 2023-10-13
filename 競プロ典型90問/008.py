"""
・sを先頭から見ていく
・i文字目がtであるとき、i文字目までで作れる"at"はi文字目までで出現するaの数
・i文字目がcであるとき、i文字目までで作れる"atc"はi文字目までで作ることのできるatの数(上のもの)
・上記の考えに基づいて、カウントしていく
・1文字ずつ見ていくので計算量はO(N)
"""

from collections import defaultdict
mod = 10**9+7
n = int(input())
s = input()

atcoder = 'atcoder'
d = defaultdict(int)

for i in s:
    if i not in atcoder: continue
    idx = atcoder.index(i)
    if idx==0:
        d[idx] += 1
    else:
        d[idx] += d[idx-1]
    d[idx] %= mod

print(d[atcoder.index('r')]%mod)