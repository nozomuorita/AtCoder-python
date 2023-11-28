n, k = map(int, input().split())
a = list(map(int, input().split()))

a = list(set(a))
a.sort()

ans = 0
for i in range(len(a)):
    if (i+1)<=k and a[i]==ans:
        ans += 1
    else: break

print(ans)