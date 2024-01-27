n = int(input())

if n%2==1: exit(print(0))

ans = 0

p = 10
while n//p!=0:
    ans += n//p
    p *= 5
    
print(ans)