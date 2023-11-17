"""
・いもす法のような考え方
・lに+1してr+1に-1する
・累積和をとる
・累積和をとったものは、各こまが何回裏返されたかを表す
・偶数なら表、奇数なら裏となる
"""
n, q = map(int, input().split())
f = [0]*(n+1)

for i in range(q):
    l, r = map(lambda x: x-1, map(int, input().split()))
    f[l] += 1
    f[r+1] -= 1
    
for i in range(1, n+1):
    f[i] = f[i-1] + f[i]
    
ans = ""
for i in f[:-1]:
    ans+="0" if i%2==0 else "1"
print(ans)