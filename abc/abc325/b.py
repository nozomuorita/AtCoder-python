n = int(input())
wx = [list(map(int, input().split())) for _ in range(n)]

ans = -1
for i in range(24):    # 世界標準時で0~23時に会議を開始するとする
    t = 0
    for w, x in wx:
        if 9<=(i+x)%24<=17: t += w     #  x時間ずれた(進んだ)時間が9~17時以内なら足す(0~23時になるよう24のmodをとる)
    ans = max(ans, t)
    
print(ans)