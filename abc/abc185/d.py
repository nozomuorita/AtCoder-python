def ceil_div(x, y): return -(-x//y)
n, m = map(int, input().split())
a = list(map(int, input().split()))

if 1 not in a: a.insert(0, 0)
if n not in a: a.insert(m+1, n+1)
a.sort()

mn = 10**18
for i in range(len(a)-1):
    if a[i+1]-a[i]-1==0: continue
    mn = min(mn, a[i+1]-a[i]-1)

ans = 0
if mn!=0:
    for i in range(len(a)-1): ans+=ceil_div((a[i+1]-a[i]-1), mn)
print(ans)