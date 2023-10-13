"""
・Xの解説参照
"""

mod = 10**9+7
n = int(input())
ans = 1
for i in range(n):
    a = list(map(int, input().split()))
    s = sum(a)
    ans *= s
    ans %= mod
    
print(ans)