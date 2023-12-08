#!/usr/bin/python
# -*- coding: utf-8 -*-
from collections import defaultdict
import sys
sys.setrecursionlimit(10000000)

n, t, m = map(int, input().split())
rel = defaultdict(set)
for i in range(m):
    a, b = map(lambda x: x-1, map(int, input().split()))
    rel[a].add(b)
    rel[b].add(a)

ans = 0

teams = []
def dfs(i):
    global ans
    if i==n:
        if len(teams)==t: ans+=1
    else:
        if not teams:                #  teams‚ª‹ó‚È‚ç
            teams.append(set())
            teams[-1].add(i)
            dfs(i+1)
            teams.pop()
        else:
            if len(teams)<t:
                teams.append(set())
                teams[-1].add(i)
                dfs(i+1)
                teams.pop()
            for j in range(len(teams)):
                if not(teams[j] & rel[i]):
                    teams[j].add(i)
                    dfs(i+1)
                    teams[j].discard(i)

dfs(0)
print(ans)
