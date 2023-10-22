n, m = map(int, input().split())
s = []
for i in range(m):
    lst = list(map(int, input().split()))
    s.append(lst[1:])
    
p = list(map(int, input().split()))

ans = 0
for i in range(2**n):
    on = [0]*m
    for j in range(n):
        if (i>>j) & 1:
            for k in range(m):
                if j+1 in s[k]:
                    on[k] += 1
        
    f = True
    for k in range(m):
        if on[k]%2==p[k]: continue
        else: f = False; break
    
    if f: ans += 1
    
print(ans)