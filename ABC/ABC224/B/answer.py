h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

for i1 in range(h):
    for j1 in range(w):
        for i2 in range(h):
            for j2 in range(w):
                # グリッドの範囲を満たす場合に条件を判定
                if (0<=i1<i2<=h-1) and (0<=j1<j2<=w-1):
                    if a[i1][j1]+a[i2][j2] <= a[i2][j1]+a[i1][j2]:
                        continue
                    else:
                        print('No')
                        exit()

print('Yes')