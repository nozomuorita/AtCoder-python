import collections

n = int(input())

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
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

ans = 0
c = collections.Counter(prime_factorize(n))
for i in c:
    x = 1
    while c[i]>=x:
        ans += 1
        c[i] -= x
        x += 1
    
print(ans)

# 別解(同じアプローチ)
# from collections import defaultdict
# n = int(input())
# n2 = n

# c = defaultdict(int)
# for i in range(2, int((n**0.5))+1):
#     while n2%i==0:
#         c[i] += 1
#         n2 //= i
#     if n2==1:
#         break

# ans = 0
# if n2!=1:
#     c[n2] = 1
# for i in c:
#     x = 1
#     while c[i]>=x:
#         ans += 1
#         c[i] -= x
#         x += 1

# print(ans)