from collections import defaultdict
from bisect import bisect_left, bisect_right, insort_left, insort_right
n = int(input())
a = list(map(int, input().split()))
q = int(input())

cnt = defaultdict(list)
for i in range(n):
    cnt[a[i]].append(i+1)

for i in range(q):
    l, r, x = map(int, input().split())
    x2 = cnt[x]
    left = bisect_left(x2, l)
    right = bisect_right(x2, r)
    print(right - left)