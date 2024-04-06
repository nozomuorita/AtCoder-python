n = int(input())
a = list(map(int, input().split()))

if sum(a)%n!=0: exit(print(-1))

people = 0
ans = 0
for i in range(n-1):
    people += a[i]
    if people!=(sum(a)//n)*(i+1): ans+=1

print(ans)