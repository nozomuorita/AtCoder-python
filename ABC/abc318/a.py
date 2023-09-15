n, m, p = map(int, input().split())

if n<m:
    ans = 0
else:
    n -= m
    ans = 1
    ans += n//p
print(ans)