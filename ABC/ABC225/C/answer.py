n, m = map(int, input().split())
b = []

for i in range(n):
    b.append(list(map(int, input().split())))

# 行が１増えると、値は7増える
# 列が１増えると、値は１増える
# かつ、各行について mod 7 をとったときに小さい順に並んでいるか判定
# 上記条件に従うか判定

# 行列Aが取りうる最大値と最小値
mn = 1
mx = (10**100 - 1) * 7 + 7

for i in range(n):
    for j in range(m):
        s_0 = b[0][0]
        s = b[i][j]

        # b[i][j]が[mn, mx]の範囲に入っていないなら、No
        if (s>mx) or (s<mn):
            print('No')
            exit()

        # 左上のマスとの差分
        dif = (7 * i) + j
        # 左上との差分が異なるならNo
        if s - s_0 != dif:
            print('No')
            exit()

# mod 7 が小さい順か判定
for i in range(n):
    tmp = []
    for j in b[i]:
        if j%7 == 0:
            tmp.append(7)
        else:
            tmp.append(j%7)
    tmp2 = sorted(tmp)
    if tmp != tmp2:
        print('No')
        exit()

print('Yes')