# 和の期待値は、期待値の和
n, k = map(int, input().split())
p = list(map(int, input().split()))

# 各サイコロの期待値を事前計算
e = []
for i in range(n):
    E = (1/p[i]) * (p[i]*(p[i]+1)/2)
    e.append(E)

# 累積和
e_cum = [0]
for i in range(n):
    e_cum.append(e_cum[i]+e[i])

ans = -1
for i in range(n-k+1):
    e_sum = e_cum[i+k] - e_cum[i]
    if e_sum > ans:
        ans = e_sum

print(ans)