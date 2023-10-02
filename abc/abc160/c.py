"""
・i=0~n-1について、a[i]とa[i+1]の距離(隣り合う家の距離)を計算
・その和から一番距離のあるものを引くと答え
・n-1と0の家の距離を計算するために、aにk+a[0]を追加する
・i=n-1と0の距離は、a[n-1]とk+a[0]の距離
"""

k, n = map(int, input().split())
a = list(map(int, input().split()))
a.append(k+a[0])

dist = []
for i in range(n):
    dist.append(abs(a[i+1]-a[i]))
    
ans = sum(dist) - max(dist)
print(ans)