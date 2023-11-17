"""
・偶数番目、奇数番目ともに一番多いものに揃えるのが最適
・揃えた結果、残る数字が1種類にならないように注意
"""
from collections import defaultdict
n = int(input())
v = list(map(int, input().split()))

v1 = v[0::2]
v2 = v[1::2]
d1 = defaultdict(int)
d2 = defaultdict(int)

for i in v1: d1[i]+=1
for i in v2: d2[i]+=1

d1s = sorted(d1.items(), key=lambda x:x[1], reverse=True)
d2s = sorted(d2.items(), key=lambda x:x[1], reverse=True)

if d1s[0][0]!=d2s[0][0]: print(n-d1s[0][1]-d2s[0][1])
else:
    if len(d1s)==1 and len(d2s)==1: print(n//2)
    elif len(d1s)==1: print(n-d1s[0][1]-d2s[1][1])
    elif len(d2s)==1: print(n-d1s[1][1]-d2s[0][1])
    else:
        ans1 = n-d1s[0][1]-d2s[1][1]
        ans2 = n-d1s[1][1]-d2s[0][1]
        print(min(ans1, ans2))