# @nzm_ort
# https://github.com/nozomuorita/atcoder-workspace-python

# import module ------------------------------------------------------------------------------
from collections import defaultdict, deque, Counter
import math
from itertools import combinations, permutations, product, accumulate, groupby, chain
from heapq import heapify, heappop, heappush
import bisect
import sys
# sys.setrecursionlimit(100000000)
inf = float('inf')
mod1 = 10**9+7
mod2 = 998244353
def ceil_div(x, y): return -(-x//y)

# main code ------------------------------------------------------------------------------------
n = int(input())
s = list(input())
q = int(input())
txc = []

t_num = -1  # 最後に行われるのが小文字にする操作(2)か大文字にする操作(3)か
t_idx = -1  # 最後に2か3が行わるのは何番目のクエリか

#  t_numとt_idxを求める
for i in range(q):
    txc_ = list(map(str, input().split()))
    txc.append(txc_)
    if txc_[0]=='2':
        t_num = 2
        t_idx = i
    elif txc_[0]=='3':
        t_num = 3
        t_idx = i

#  最後に行われるのが2ならば、いったんすべて小文字に、3なら大文字に変更
if t_num==2:
    for i in range(n):
        s[i] = s[i].lower()
elif t_num==3:
    for i in range(n):
        s[i] = s[i].upper()

#  クエリが１の場合は、文字の変更操作をする
#  もし、t_idx(すべての文字を変更するクエリ)よりも前の操作ならば、どうせ書き換えられるので書き換えられる文字(大文字か小文字か)にして変更
#  t_idxより後ならば、影響はないので、入力されたcのとおりに変更
for i in range(q):
    t, x, c = int(txc[i][0]), int(txc[i][1]), txc[i][2]
    if (t==2) or (t==3):
        continue
    if i <= t_idx:
        if t_num==2:
            s[x-1] = c.lower()
        elif t_num==3:
            s[x-1] = c.upper()
    else:
        s[x-1] = c

print(''.join(s))


# for i in range(q):
#     t, x, c = map(str, input().split())
#     t = int(t)
#     if t==2:
#         t_num = 2
#         change.clear()
#     elif t==3:
#         t_num = 3
#         change.clear()
#     else:
#         x = int(x)
#         x -= 1
#         change[x] = c
#         change_all[x] = c

# for i in range(len(s)):
#     if t_num==2:
#         s[i] = s[i].lower()
#     elif t_num==3:
#         s[i] = s[i].upper()
#     else:
#         continue
# print(change)
# for key in list(change.keys()):
#     s[key] = change[key]

# print(''.join(s))