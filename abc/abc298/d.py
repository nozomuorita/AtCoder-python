from collections import deque
mod = 998244353

Q = int(input())
n = 1
d = deque()
d.append(1)
for i in range(Q):
    q = list(map(int, input().split()))
    if q[0]==1:
        d.append(q[1])
        n = (10*n) + q[1]
        n %= mod
    elif q[0]==2:
        t = d.popleft()
        n -= t*pow(10, len(d), mod)
        n %= mod
    else:
        print(n%mod)