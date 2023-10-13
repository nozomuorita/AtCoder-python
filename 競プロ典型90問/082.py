mod = 10**9+7
l, r = map(int, input().split())
ans = 0
l_keta = len(str(l))
r_keta = len(str(r))
for i in range(l_keta, r_keta+1):
    el = max(10**(i-1), l)
    er = min(10**i-1, r)
    s = ((el+er)*(er-el+1))//2
    ans += s*i
    ans %= mod
    
print(ans)