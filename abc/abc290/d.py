from math import gcd
t = int(input())
for _ in range(t):
    n, d, k = map(int, input().split())
    g = gcd(n, d)
    
    a = n//g
    ans = ((k-1)//a) + ((k-1)*d%n)
    print(ans)