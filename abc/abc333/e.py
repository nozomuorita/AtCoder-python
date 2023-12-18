#!/usr/bin/python
# -*- coding: utf-8 -*-
from collections import deque
n = int(input())
tx = [tuple(map(int, input().split())) for _ in range(n)]
portion = [deque() for _ in range(n+1)]  # portion[x]: タイプxのポーションを拾った順番

cnt = 0
for i in range(n):
    if tx[i][0]==1: cnt+=1
ans = [0]*cnt         #  出現するポーション数だけ0で初期化

crr = 0               #  現在までに登場したポーションの数
for i in range(n):
    t, x = tx[i][0], tx[i][1]
    if t==1:
        portion[x].appendleft(crr)    # タイプxにポーション番号を追加(左から)
        crr += 1                      # 登場したポーション数を1追加
    else:
        if len(portion[x])==0: exit(print(-1))   # タイプxのポーションがないなら不可(-1)
        idx = portion[x].popleft()               # 一番最後に拾ったタイプxのポーションを使う
        ans[idx] = 1                             # 使用するポーションを1にする

# kmx: 所持しているポーション数のマックス, p: 今持っているポーション数
kmx, p, crr = 0, 0, 0
for i in range(n):
    t, x = tx[i][0], tx[i][1]
    if t==1:
        if ans[crr]==1: p+=1    # ポーションを拾う場合はpに1追加
        crr += 1                
    else:
        p -= 1                  # ポーションを使用する場合は1減らす
    kmx = max(kmx, p)           # 最大所次数と今持っているポーション数で更新

print(kmx)
print(*ans)
