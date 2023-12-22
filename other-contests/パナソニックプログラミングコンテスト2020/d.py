"""
・最初の文字はaである。
・dfsでaからそれまでに登場した文字+1(bならcまで、dならeまで)を追加したもので再帰
・文字数がnならlstに追加
"""
import sys
sys.setrecursionlimit(100000000)

n = int(input())
lst = set()

# i: 文字列, cnt: 文字種類数
def dfs(i, cnt):
    if len(i)==n: lst.add(i); return
    
    for x in range(cnt+1):
        c = chr(ord("a")+x)
        if x==cnt: dfs(i+c, cnt+1)
        else: dfs(i+c, cnt)

dfs("a", 1)
ans = sorted(list(lst))
for i in ans: print(i)