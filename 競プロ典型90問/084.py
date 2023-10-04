"""
・"o"の位置と"x"の位置を、maru, batuに記録しておく
・i番目の文字について、"o"ならば、"x"の中でi以降に初めて出現する場所を二分探索で探す。
・その場所以降はすべて成立する区間であるため、個数を計算してansに追加
・ex) ooxo の場合
・s[0]="o"について、s[0]以降で初めて出現する"x"はs[2]="x"である。
・ゆえに、i=2以降はすべて成立し、(0, 2), (0, 3)がi=0についての答えとなる
・このことから、二分探索で初めて"x"となるインデックス2を取得し、nから引くことでn-idx=4-2=2個となり、i=0について成立する区間が求まる。
・注意)二分探索した時に、取得したインデックスが範囲外である場合、i以降に出現する異なる文字がないことになるので、この場合は足さない(足せない)
"""
from bisect import bisect_left, bisect_right, insort_left, insort_right
n = int(input())
s = input()

maru, batu = [], []
for i in range(n):
    if s[i]=='o':
        maru.append(i)
    else:
        batu.append(i)

ans = 0
for i in range(n):
    if s[i]=='o':
        idx = bisect_right(batu, i)
        if idx<len(batu): ans += n-batu[idx]
    else:
        idx = bisect_right(maru, i)
        if idx<len(maru): ans += n-maru[idx]
print(ans)

# """
# ・公式解法
# """
# n = int(input())
# s = input()

# ans = (n*(n-1))//2
# t = s[0]
# num = 1
# for i in range(1, n):
#     if s[i]==t:
#         num += 1
#     else:
#         ans -= (num*(num-1))//2
#         t = s[i]
#         num = 1

# ans -= (num*(num-1))//2
# print(ans)