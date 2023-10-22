n = int(input())
ns = str(n)
ans = 0

for i in range(4, len(ns)+1):
    t = int('9'*(i-1))+1
    if n<t: break
    
    c = (i-1)//3
    ans += (min(n, int('9'*i))-t+1)*c

print(ans)