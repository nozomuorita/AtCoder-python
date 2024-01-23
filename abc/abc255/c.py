x, a, d, n = map(int, input().split())

if d==0: exit(print(abs(x-a)))
if d<0:
    a = a + (d*(n-1))
    d *= -1

an = a + ((n-1)*d)

if x<a:
    exit(print(abs(a-x)))
if an<x:
    exit(print(abs(x-an)))

ans = 10**18
tmp = (x-a)//d
if a<=(a+tmp*d)<=an: ans=min(ans, abs(x-(a+tmp*d)))
tmp += 1
if a<=(a+tmp*d)<=an: ans=min(ans, abs(x-(a+tmp*d)))

print(ans)