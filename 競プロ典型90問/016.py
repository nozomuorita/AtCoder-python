"""
・a, bを固定して、cが成立するか判定し、最小枚数を求める
・a, bを固定すると、計算量はO(10000**2)=O(10**8)であり、なんとか可能である
"""

n = int(input())
a, b, c = map(int, input().split())

ans = 10**18
for i in range(10000):
    for j in range(10000-i):
        if i+j>=9999: continue
        if (a*i)+(b*j)>n: continue
        m = n - (a*i) - (b*j)
        t = i+j
        if (m%c==0):
            ans = min(ans, t+(m//c))

print(ans)