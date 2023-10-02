"""
・二分探索
・aをi冊読むとして、bが何冊読めるか探索
・手順
・a、bの累積和を計算しておく
・aをi冊読むとすると、累積和からaの本だけで何分要するかわかる
・kからaで要する時間を引くことで、bに何分使うことができるかを計算
・bの累積和から二分探索でbに使うことのできる時間を探索し、何冊読めるのかを求める
・bで読むことのできる冊数を足して、ansが更新されるなら更新
"""

from bisect import bisect_left, bisect_right, insort_left, insort_right

n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_cum, b_cum = [0], [0]
for i in range(n):
    a_cum.append(a_cum[i]+a[i])
for i in range(m):
    b_cum.append(b_cum[i]+b[i])

ans = -1
for i in range(len(a_cum)):
    if a_cum[i]>k: continue
    num = i
    s = k-a_cum[i]
    idx = bisect_right(b_cum, s)
    num += idx-1
    ans = max(ans, num)
    
print(ans)