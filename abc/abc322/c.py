from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right, insort_left, insort_right

n, m = map(int, input().split())
a = list(map(int, input().split()))
    
for i in range(1, n+1):
    idx = bisect_left(a, i)
    print(a[idx]-i)