from bisect import bisect_left, bisect_right, insort_left, insort_right
n = int(input())
a = sorted(list(map(int, input().split())))
q = int(input())
for _ in range(q):
    b = int(input())
    idx = bisect_left(a, b)
    
    print(min(abs(a[min(idx, n-1)]-b), abs(a[max(idx-1, 0)]-b)))