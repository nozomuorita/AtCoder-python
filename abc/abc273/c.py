from bisect import bisect_left, bisect_right, insort_left, insort_right
n = int(input())
a = list(map(int, input().split()))
a_sorted = sorted(set(a))
num = len(set(a))

ans = [0]*n
for i in range(n):
    idx = bisect_right(a_sorted, a[i])
    ans[num-idx] += 1

for i in ans: print(i)