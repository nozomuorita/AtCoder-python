n, m = map(int, input().split())
b = []

for i in range(n):
    b.append(list(map(int, input().split())))

# 行が１増えると、値は7増える
# 列が１増えると、値は１増える
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

print('Yes')