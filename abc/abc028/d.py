n, k = map(int, input().split())

# kが1回のとき
k1 = (n-k) * (k-1) * 6
# kが2回のとき
k2 = (n-1) * 3
# kが3回のとき
k3 = 1

ans = (k1+k2+k3) / (n**3)
print(ans)