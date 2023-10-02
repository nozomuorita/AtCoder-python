n, p, q = map(int, input().split())
a = list(map(int, input().split()))
ans = 0

# 余りとしておく
r = []
for i in range(n):
    r.append(a[i]%p)

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            for l in range(k+1, n):
                for m in range(l+1, n):
                    # かけるごとにあまりにしていく
                    tmp = (((((((r[i]*r[j])%p) * r[k])%p) * r[l])%p) * r[m])
                    if (tmp%p)==q:
                        ans += 1

print(ans)