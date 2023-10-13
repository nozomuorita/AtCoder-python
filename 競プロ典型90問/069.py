"""
・パターン数はk*(k-1)*((k-1)**n-2)となるため、powで計算
・コーナーケース(nやkが小さい場合に注意1)
"""
mod = 10**9+7
n, k = map(int, input().split())

if n==1:
    print(k)
    exit()

if n==2:
    if k==1:
        print(0)
        exit()
    else:
        print(k*(k-1))
        exit()

# 色が2種類以下なら不可
if n>=3 and k<=2:
    print(0)
    exit()
    
ans = pow(k-2, n-2, mod)
ans *= k-1
ans %= mod
ans *= k
ans %= mod
print(ans)