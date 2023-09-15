"""
・全探索
・各マスについて、"#"であれば縦横斜め方向に6マス分探索する
・"#"でないもの、すなわち、"."であるものが二つ以下であれば、Yesである。
・全マス探索して、見つからなければNo
・各マスについて8方向に6マス分探索するため、ざっとO(8*6*(n**2))で間に合う。
※キューでなく、for文で6マス分探索でもよいかも
"""

from collections import deque
n = int(input())
s = [list(input()) for _ in range(n)]

# 8方向それぞれの差分をリストにする
dist = []
for i in range(-1, 2):
    for j in range(-1, 2):
        if (i==0) and (j==0):
            continue
        dist.append((i, j))

for i in range(n):
    for j in range(n):
        # "."なら飛ばす
        if s[i][j]=='.':
            continue
        
        # 8方向について一つずつ見ていく
        for d1, d2 in dist:
            # キューを用いて探索((i, j)を始点とする)
            q = deque([(i, j)])
            m = 0                 # "#"の数(置換した"."も含む)
            p = 0                 # 置換した数("."の数)
            while q:
                i2, j2 = q.popleft()
                # グリッドの範囲外なら、whileを抜ける(トーラスは成していないので反対側に移動することはできない)
                if (not(0<=i2<n)) or (not(0<=j2<n)):
                    break
                # "#"ならば、mを加算
                if s[i2][j2] == '#':
                    m += 1
                # "."の場合、置換できるなら置換してpとmを加算、置換できないときは、mが6でないならば不可なのでwhileを抜ける
                else:
                    if p<2:
                        p += 1
                        m += 1
                    else:
                        if m != 6:
                            break
                
                # "#"が6ならば、見つけたことになるので、Yesで終了
                if m==6:
                    print('Yes')
                    exit()
                # そうでないなら、d1, d2だけ移動した座標をキューに追加し、探索
                else:
                    q.append((i2+d1, j2+d2))
                    
print('No')