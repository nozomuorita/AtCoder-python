"""
・m個の操作方法のうち、cが大きいものから操作する
・aをheapqで管理し、小さいほうから取り出して、cの方がでかいなら置き換え
・aの最小値の方が大きいならそれ以降の操作は不要
・操作する回数は最大でも、len(a)なので、間に合う
"""
from heapq import heapify, heappop, heappush
n, m = map(int, input().split())
a = list(map(int, input().split()))
heapify(a)

# cb = sorted([[j, i] for i, j in [map(int, input().split()) for _ in range(m)]], reverse=True)

cb = []
for i in range(m):
    b, c = map(int, input().split())
    cb.append([c, b])
cb.sort(reverse=True)

for i in range(m):
    c, b = map(int, cb[i])
    for j in range(b):
        num = heappop(a)
        if c>num:
            heappush(a, c)
        else:
            heappush(a, num)
            break
    else:
        continue
    break

print(sum(a))