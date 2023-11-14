from bisect import bisect_left
n, q = map(int, input().split())
a = list(map(int, input().split()))

d = [a[0]-1]
for i in range(1, n): d.append(d[-1]+(a[i]-a[i-1]-1))

for i in range(q):
    k = int(input())
    if k>d[-1]: print(a[-1]+(k-d[-1]))
    else:
        idx = bisect_left(d, k)
        print(a[idx]-1-(d[idx]-k))