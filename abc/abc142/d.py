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

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

a, b = map(int, input().split())

a_div = make_divisors(a)
b_div = make_divisors(b)

#  aとbの公約数
ab_div = set(a_div) & set(b_div)

ans = 1
for i in ab_div:
    if i==1: continue
    if is_prime(i): ans+=1
    
print(ans)