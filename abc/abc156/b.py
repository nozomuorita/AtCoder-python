n, k = map(int, input().split())
ans = 0
while (n != 0):
    r = n % k
    n //= k

    if (n!=0):
        ans += 1
print(ans+1)