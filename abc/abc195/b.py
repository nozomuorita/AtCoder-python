a, b, w = map(int, input().split())
w *= 1000

# n個買うことができるかを調べる。
# 最大で1 * 1000 * 1000

mn = 10**9
mx = 0
for i in range(1, 1000*1000+1):
    if a*i <= w <= b*i:
        mn = min(mn, i)
        mx = max(mx, i)

if mx == 0:
    print('UNSATISFIABLE')
else:
    print(mn, mx)