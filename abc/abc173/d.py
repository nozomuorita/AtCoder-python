"""
・フレンドリーさが大きいほうから、入れるのが最適な行動となる
・最適な場所に入れていくと、フレンドリーさが大きいほうからA、B、C、D、Eとすると以下のようになる
・max(score)=A+B+B+C+C+D+D+E+E+...
・よってこれを計算する
・上記事項はシミュレーションすることで確認できる
"""

n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
ans = a[0]

t = 1
s = 0
for i in range(2, n):
    if s==0:
        ans += a[t]
        s += 1
    else:
        ans += a[t]
        t += 1
        s = 0
        
print(ans)