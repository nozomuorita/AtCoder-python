"""
・無色のリンゴを1個使う場合、2個使う場合...c個使う場合と考えて「無色のリンゴを使用する個数」について全探索する
・無色のリングをi個使う場合、おいしさが大きいほうからとると良いので、累積和を計算しておく
・無色のリンゴをi個使った場合、赤、緑のリンゴはx+y-i個選択する必要がある。
・これは、赤いリンゴからおいしいものx個、緑からおいしいものy個取り出した和集合から、おいしい順にx+y-i個選択することである。
・これにより、赤いリンゴは最大でx個、緑は最大でy個選択されるので、xとyの条件を満たした状態で最良の選択ができる。
"""

x, y, a, b, c = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p.sort(reverse=True)
q.sort(reverse=True)
r.sort(reverse=True)

# 無色のリンゴについて累積和を計算
r_cum =[0]
for i in range(c):
    r_cum.append(r_cum[i]+r[i])
        
# 赤、緑のリンゴについて累積和を計算(赤はx個、緑はy個)
pq = p[:x] + q[:y]
pq.sort(reverse=True)
pq_cum = [0]
for i in range(x+y):
    pq_cum.append(pq_cum[i] + pq[i])
    
# 無色のリンゴをi個使用するとして、全探索
ans = 0
for i in range(c+1):
    if i<=(x+y):
        s = r_cum[i]
        s += pq_cum[x+y-i]
    else:
        s = r_cum[x+y]
    if s > ans:
        ans = s

print(ans)