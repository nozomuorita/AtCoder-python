n = int(input())
a = [list(input()) for _ in range(n)]

# 計算量を減らすために、aの中の最大の数を求めておく(答えの先頭はa内の最大の数であるため、それ以外であればパスするため)
mx = '0'
for i in range(n):
    for j in range(n):
        if a[i][j]>mx:
            mx = a[i][j]

# 初期値はすべて0としておく
ans = ['0'] * n
# すべてのマスをスタート地点としてfor文を回す
for i in range(n):
    for j in range(n):
        # 最大の値でないなら、答えにはなりえないのでパス
        if a[i][j] != mx:
            continue
        # 8方向の変化量でfor文を回す
        for d1, d2 in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, -1], [-1, -1], [1, 1], [-1, 1]]:
            i2, j2 = i, j
            # 一番最初の数は、最大の値である
            tmp = [mx] + (['0']*(n-1))
            # ２番目の文字から埋めていく
            for k in range(1, n):
                # 変化量だけ座標を移動する(グリッドの範囲を超えないように、modをとる)
                i2 = (i2+d1) % n
                j2 = (j2+d2) % n
                # 移動後の場所の数をtmpに追加
                tmp[k] = a[i2][j2]
            # ansよりも大きいなら、更新
            if tmp > ans:
                ans = tmp
print(''.join(ans))