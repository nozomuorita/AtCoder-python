mod = 998244353
n, m = map(int, input().split())

ans = 0

k = []
for i in range(len(bin(m))-2):
    if m>>i & 1:
        k.append(i)

for i in k:
    score = 0
    tmp = n - (2**i-1)
    
    score += (tmp // (2**(i+1))) * (2**i)
    score += min((tmp%(2**(i+1))), 2**i)
    ans += score
    ans %= mod

print(ans)