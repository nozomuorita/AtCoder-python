"""
・各bitごとに考える
・累積XOR
"""

n = int(input())
a = list(map(int, input().split()))

a_cum_xor = [0]
for i in range(n):
    a_cum_xor.append(a_cum_xor[-1]^a[i])

ans = 0

for i in range(len(bin(max(a)))-2):
    zero, one = 0, 0
    for j in range(len(a_cum_xor)):
        if (a_cum_xor[j]>>i) & 1:
            one += 1
        else:
            zero += 1
    
    ans += (one * zero) * (2**i)

print(ans - sum(a))