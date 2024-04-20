n = int(input())
ans = 0
for i in range(1, 10**6+1):
    k = str(i**3)
    if k==k[::-1] and int(k)<=n:
        ans = max(ans, int(k))
    if int(k)>n:
        break
print(ans)