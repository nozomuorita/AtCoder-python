n, s, t = map(int, input().split())
w = int(input())
a = []
for i in range(n-1):
    a_ = int(input())
    a.append(a_)
    
ans = 0
if s<=w<=t:
    ans += 1
    
for i in a:
    w += i
    if s<=w<=t:
        ans += 1
        
print(ans)