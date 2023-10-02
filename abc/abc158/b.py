n, a, b = map(int, input().split())

ans = (n//(a+b)) * a
n = n % (a+b)
if n<=a:
    ans += n
else:
    ans += a
print(ans)