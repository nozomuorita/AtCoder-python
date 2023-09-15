n, l = map(int, input().split())

s = 0
for i in range(n):
    s += l + (i+1) - 1
    
dist = 10**10
ans = 10**10
for i in range(n):
    tmp = s
    tmp -= l + (i+1) - 1
    if abs(tmp-s) < dist:
        ans = tmp
        dist = abs(tmp-s)
        
print(ans)