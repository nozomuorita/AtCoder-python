n, m = map(int, input().split())
a = list(map(int, input().split()))

# 累積和
c = [0]
for i in range(n): c.append(c[-1]+a[i])

ans = 0
for i in range(m):
    ans += (i+1)*a[i]

tmp = ans
for i in range(1, len(a)-m+1):
    tmp -= c[i+m-1]-c[i-1]
    tmp += m*a[i+m-1]

    ans = max(ans, tmp)
    
print(ans)