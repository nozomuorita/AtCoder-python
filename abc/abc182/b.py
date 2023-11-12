from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

d = defaultdict(int)
for i in range(n):
    m = make_divisors(a[i])
    for j in m:
        if j==1: continue
        d[j] += 1

ans = 2
mx = -1
for key in list(d.keys()):
    if d[key]>mx:
        ans = key
        mx = d[key]
        
print(ans)