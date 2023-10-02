n = int(input())

ans = 0
# cnt[i][j]: topがiでbtmがjである数の個数
cnt = [[0]*10 for _ in range(10)]
for i in range(1, n+1):
    atop = int(str(i)[0])
    abtm = int(str(i)[-1])
    cnt[atop][abtm] += 1
    
for i in range(10):
    for j in range(10):
        if cnt[i][j]>0:
            ans += cnt[i][j] * cnt[j][i]

print(ans)