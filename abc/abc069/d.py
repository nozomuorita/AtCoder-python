import sys
sys.setrecursionlimit(10000000)
h, w = map(int, input().split())
c = [[-1]*w for _ in range(h)]
n = int(input())
a = list(map(int, input().split()))

a_cum = [0]
for i in a: a_cum.append(a_cum[-1]+i)

idx = 1
num = 0
for i in range(h):
    for j in range(w):
        c[i][j] = idx
        num += 1
        if num>=a_cum[idx]: idx+=1

for i in range(h):
    print(*c[i]) if i%2==0 else print(*list(reversed(c[i])))
