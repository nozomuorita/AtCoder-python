"""
・aの各要素について、その倍数はすべて約数を持つことになるので、条件を満たさないということがわかる
・辞書で、各要素の倍数を数えることで、それぞれの数が条件を満たすか判定できる
"""

from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
a.sort()
mx = max(a)

ans = 0
d = defaultdict(int)

for i in a:
    t = i
    d[t] += 1
    while t<=mx:
        t += i
        d[t] += 1

ans = 0
for i in a:
    if d[i]==1:
        ans += 1

print(ans)