n, k, m = map(int, input().split())
a = list(map(int, input().split()))

sum_ = sum(a)
ans = (m*(len(a)+1))
ans -= sum_

if ans>k:
    print(-1)
elif ans<0:
    print(0)
else:
    print(ans)