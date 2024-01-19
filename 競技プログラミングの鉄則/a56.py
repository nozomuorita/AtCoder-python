n, q = map(int, input().split())
s = input()
mod = 998244353

# 文字列を数値に変換
t = []
for i in s: t.append(ord(i)-ord("a"))

# B=100とする
# 100のn乗を前計算
power = [1]
for i in range(n):
    power.append(power[i]*100%mod)

# ハッシュ値h1, h2, ...hnを計算
h = [0]
for i in range(n):
    h.append((h[i]*100 + t[i])%mod)

for _ in range(q):
    a, b, c, d = map(int, input().split())
    
    hash_ab = (h[b] - (power[b-a+1] * h[a-1])) % mod
    hash_cd = (h[d] - (power[d-c+1] * h[c-1])) % mod
    
    print('Yes') if hash_ab==hash_cd else print('No')