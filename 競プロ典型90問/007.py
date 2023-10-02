"""
・二分探索で、最も近い場所を探し、その付近で差が最小のものを出力
"""

from bisect import bisect_left, bisect_right, insort_left, insort_right

n = int(input())
a = list(map(int, input().split()))
a.sort()

q = int(input())
b = [int(input()) for _ in range(q)]
ans = 0
for i in range(q):
    idx = bisect_left(a, b[i])
    if idx==len(a):
        print(abs(b[i]-a[idx-1]))
    elif idx==0:
        print(abs(b[i]-a[0]))
    else:
        print(min(abs(b[i]-a[idx]), abs(b[i]-a[idx-1])))