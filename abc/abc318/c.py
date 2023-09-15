# 値段の高い日からパスを使用していく
# パスを買える上限をm枚として、0枚使ったとき、1枚使ったとき、...として最小を求める

def ceil_div(x, y): return -(-x//y)

n, d, p = map(int, input().split())
f =list(map(int, input().split()))

f.sort(reverse=True) # 値段の高い順にソート
m = ceil_div(n, d)   # m: 購入できる最大枚数(m以上も買うことはできるが使うことはないので無駄になる)

fee = sum(f)         # fee: すべて通常料金で買ったとき
tmp = fee

# パスを買う枚数をiとしてfor文を回す
for i in range(m):
    # パスの日数分、料金の高いほうから使用していく
    for j in range(d):
        # もし、使える日があるならまだ使っていない日で、一番高い日に使う(その日の料金を引く)
        if d*i+j <= n-1:
            tmp -= f[d*i+j]
        else:
            break
    # パスの料金を足す
    tmp += p
    # 安くなるなら更新
    if tmp < fee:
        fee = tmp
    #print(fee)
        
print(fee)