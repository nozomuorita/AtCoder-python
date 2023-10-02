import math
import functools
def my_gcd(*integers): return functools.reduce(math.gcd, integers)

k = int(input())
ans = 0

for a in range(1, k+1):
    for b in range(1, k+1):
        for c in range(1, k+1):
            ans += my_gcd(a, b, c)
            
print(ans)