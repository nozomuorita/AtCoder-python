import bisect

n, q = map(int, input().split())
a = list(map(int, input().split()))
X = [int(input()) for _ in range(q)]

# 二分探索なので、ソート
a.sort()

for x in X:
    # 二分探索で、xが挿入されるインデックスを取得
    num = bisect.bisect_left(a, x)

    # インデックスnumより、右側にいる人数はnumを総人数nから引いた値
    ans = n - num
    print(ans)