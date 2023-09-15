n = int(input())

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

ans = ''
yakusuu = make_divisors(n)
y = []
for i in yakusuu:
    if i <= 9:
        y.append(i)
    else:
        break

for i in range(n+1):
    tmp = []
    for j in y:
        if i % (n//j)==0:
            tmp.append(j)
    if len(tmp)==0:
        ans += '-'
    else:
        ans += str(min(tmp))
        
print(ans)