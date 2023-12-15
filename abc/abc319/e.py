# -*- coding: utf-8 -*-
from math import lcm
n, x, y = map(int, input().split())
times = [0]*1000     # 時刻iに出発するときの合計時間
pt = [list(map(int, input().split())) for _ in range(n-1)]
l = 1
for i in range(n-1): l=lcm(l, pt[i][0])

for i in range(l):
    score = x+i
    for j in range(n-1):
        score = ((score-1)//pt[j][0]+1) * pt[j][0] + pt[j][1]
    score += y
    times[i] = score-i
print(times[:20])

Q = int(input())
for _ in range(Q):
    q = int(input())
    ans = q%l
    print(q + times[ans])

