n, k = map(int, input().split())
if n>=k:
    ans = n%k
else:
    ans = n
ans = min(ans, abs(ans-k))

print(ans)