n, s, m, l = map(int, input().split())
ans = float("inf")
for i in range(20):
    for j in range(20):
        for k in range(20):
            score = 6*i + 8*j + 12*k
            if score<n: continue
            price = s*i + m*j + l*k
            ans = min(ans, price)
print(ans)