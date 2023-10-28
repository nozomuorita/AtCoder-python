"""
・解説: drken
"""

n = int(input())
a = list(map(int, input().split()))
ans = []

c = 0
for i in range(n):
    c ^= a[i]
    
for i in range(n):
    c2 = c ^ a[i]
    ans.append(c2)
    
print(*ans)