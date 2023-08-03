# 前半と後半をが入れ替わるかどうかをboolで管理

n = int(input())
s = list(input())
q = int(input())

# クエリ２が起きるごとに反転(Trueなら前後半逆とする)
f = False

for i in range(q):
    t, a, b = map(int, input().split())

    if t==1:
        a -= 1
        b -= 1

        # fがTrueなら、前後半入れ替えである
        # aとbを入れ替え後のインデックスに置き換える
        if f:
            # 前後半入れ替え
            if a<=(n-1):
                a += n
            else:
                a -= n
            if b<=(n-1):
                b += n
            else:
                b -= n

        # swap
        s[a], s[b] = s[b], s[a]

    # クエリ２のときはfを反転する
    else:
        f = not(f)

# 最後にfがTrueなら反転して出力
if f:
    ans = ''.join(s[n:]) + ''.join(s[:n])
    print(ans)
else:
    print(''.join(s))
