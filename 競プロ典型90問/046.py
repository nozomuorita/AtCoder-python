"""
・(A+B+C)%46==0である組合せを求めたい
・これは以下のように置き換えても同様である
・((A%46)+(B%46)+(C%46))==0
・よって、A, B, Cについてそれぞれ、46で割った余りの個数を求めておくことで個数を調べることができる
・46で割った余りは0~45の46通りしかないので全探索することで求まる
"""

from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

da, db, dc = defaultdict(int), defaultdict(int), defaultdict(int)

for i in range(n):
    da[a[i]%46] += 1
    db[b[i]%46] += 1
    dc[c[i]%46] += 1
    
ans = 0
for i in list(da.keys()):
    for j in list(db.keys()):
        for k in list(dc.keys()):
            if (i+j+k)%46==0:
                ans += da[i]*db[j]*dc[k]
                
print(ans)