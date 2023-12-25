"""
・一桁ずつ見ていき、i桁の数をすべてあるならば、その分足す
・すべてないなら、nまでの数で整数和を計算
"""
n = int(input())
mod = 998244353

ans = 0
num = 10
for i in range(18):
    if n>=num:
        t = num - (num//10)
        ans += (1+t)*t//2
        ans %= mod
        num *= 10
    else:
        t = n - (num//10) + 1
        ans += (1+t)*t//2
        ans %= mod
        break
    
print(ans)