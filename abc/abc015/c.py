"""
・全探索(dfs)
"""
import sys
sys.setrecursionlimit(100000000)
n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]

def dfs(lst):
    if len(lst)==n:
        s = 0
        for i in lst:
            s ^= i
        if s==0: exit(print('Found'))
        return

    for j in t[len(lst)]:
        dfs(lst+[j])

dfs([])
print('Nothing')