"""
・累積和からkとなる場所を二分探索する -> kとなる場所を二分探索すれば、それ以上の長さの部分列はすべて成り立つ
・i番目からの部分列を見るときは、k+(i-1番目までの累積和)を二分探索することでi番目からの部分列でk以上となる場所がわかる
"""
from bisect import bisect_left, bisect_right, insort_left, insort_right

n, k = map(int, input().split())
a = list(map(int, input().split()))

c = [0]
for i in range(n): c.append(c[-1]+a[i])

ans = 0
for i in range(n):
    idx = bisect_left(c, k)
    ans += len(c) - idx
    k += a[i]
    
print(ans)