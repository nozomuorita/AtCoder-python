"""
・defaultdictは少し遅い？
・while len(number)>k のところ、len(list(number.keys()))とするとTLE
・キーの数を知りたいならlen(number)で良い
"""
from collections import defaultdict
n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = -1
l, r = 0, 0
number = defaultdict(int)

while r<n:
    number[a[r]] += 1
    while len(number)>k:
        number[a[l]] -= 1
        if number[a[l]]==0: del number[a[l]]
        l += 1
    
    ans = max(ans, r-l+1)
    r += 1
    
print(ans)