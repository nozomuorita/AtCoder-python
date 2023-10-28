"""
・解説(O(n**1.5))
"""

n = int(input())
ans = 0

h = []
i = 2
while True:
    if i**2>n: break
    h.append(i**2)
    i += 1

for i in range(1, n+1):
    k = i
    for x in h:
        if x>k: break
        while (k%x==0): k/=x
    
    j = 1
    while True:
        if k*(j**2)>n: break
        ans += 1
        j += 1
        
print(ans)