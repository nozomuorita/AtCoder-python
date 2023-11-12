A, B, C, D, E, F, X = map(int, input().split())

def solve(x, y, z, w):
    dist = 0 # 総距離
    period = w // (x+z) # 完了できる周期
    # 完了できる周期の分だけ距離を足す
    dist += period * (x*y)
    # 残りの時間について進める秒を計算
    t = w - (period*(x+z)) # wから完了できる周期分の時間を引いたもの→残りの時間

    # tがxより大きいならx秒間だけ進める
    if t>= x:
        dist += x*y
    # tがxより小さいなら、t秒間だけ進める
    else:
        dist += t*y
    
    return dist

takahashi = solve(A, B, C, X)
aoki = solve(D, E, F, X)

if takahashi > aoki:
    print('Takahashi')
elif takahashi < aoki:
    print('Aoki')
else:
    print('Draw')