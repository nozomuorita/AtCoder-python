"""
・いもす法
・典型を少しいじった感じ
"""
from collections import defaultdict
n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

d = defaultdict(int)            # ログイン初日を+1、ログインしなくなった日を-1
for i in range(n):
    a, b = ab[i][0], ab[i][1]
    d[a] += 1
    d[a+b] -= 1

keys = sorted(list(d.keys()))
d2 = defaultdict(int)          # 足し合わせると各日のログイン人数になる(keys2[i-1]からkeys2[i]-1日までd2[keys2[i-1]]人ログインしていた)
d2[keys[0]] = d[keys[0]]
for i in range(1, len(keys)):
    d2[keys[i]] = d2[keys[i-1]] + d[keys[i]]

ans = [0]*(n+1)  #  ans[i]: i人が同時にログインしていた日数
keys2 = list(d2.keys())
for i in range(1, len(keys2)):
    days = keys2[i] - keys2[i-1]      #  keys2の差分が同じ人数ログインしていた日数(その人数はd2[keys2[i-1]])
    ans[d2[keys2[i-1]]] += days
    
for i in range(1, n+1): print(ans[i])