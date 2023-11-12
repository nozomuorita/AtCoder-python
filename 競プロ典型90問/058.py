"""
・周期性
"""
n, k = map(int, input().split())
vis = [False]*(10**5+1)

appear = []
while vis[n]==False and k>0:
    k -= 1
    vis[n] = True
    appear.append(n)
    tmp = str(n)
    s = 0
    for i in tmp: s+=int(i)
    n = (n+s)%(10**5)

if k==0: exit(print(n))
idx = appear.index(n)
appear = appear[idx:]
k %= len(appear)

ans = appear[k]
print(ans)