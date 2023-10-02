n = int(input())
a = list(map(int, input().split()))

a_cum = [0]
for i in range(n):
    a_cum.append(a_cum[i]+a[i])

ans = 0
for i in range(n):
    ans += a[i] * (a_cum[-1]-a_cum[i+1])
    ans %= (10**9)+7

print(ans%((10**9)+7))