"""
・シンプルに条件を満たす数列を全列挙して判定
"""

import sys
sys.setrecursionlimit(100000000)

n, m, q = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(q)]
ans = 0

def dfs(lst):
    global ans, n
    if len(lst)==n:                           #  長さがnになったなら、lstが各条件を満たすか判定
        t = 0
        for a, b, c, d in abcd:
            if lst[b-1]-lst[a-1]==c: t+=d
        ans = max(ans, t)
        return
    
    x = lst[-1]                               #  lstの最後の要素を取得し、その数字からmまでの数をappendしてdfs
    for i in range(x, m+1):
        lst2 = lst.copy()
        lst2.append(i)
        dfs(lst2)
        
for j in range(1, m+1):                       #  最初の数字は1~m
    dfs([j])

print(ans)