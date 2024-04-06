from collections import Counter, defaultdict
n = int(input())
a = list(map(int, input().split()))
ans = 0

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else: f += 2
    if n != 1: a.append(n)
    return a

zero = 0

d = defaultdict(list)
for i in range(n):
    if a[i]==0:
        zero += 1
        continue
    c = Counter(prime_factorize(a[i]))
    score = 1
    
    for key in c:
        if c[key]%2!=0:
            score *= key
    
    if score==1: d[0].append(a[i])
    else: d[score].append(a[i])

for key in list(d.keys()):
    l = len(d[key])
    ans += (l*(l-1)) // 2

ans += zero * (n-1)
ans -= (zero*(zero-1)) // 2

print(ans)