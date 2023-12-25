from bisect import bisect_left, bisect_right, insort_left, insort_right
n, q = map(int, input().split())
r = sorted(list(map(int, input().split())))

sr = [r[0]]
for i in range(1, len(r)):
    sr.append(sr[-1]+r[i])

for _ in range(q):
    x = int(input())
    idx = bisect_right(sr, x)
    print(idx)