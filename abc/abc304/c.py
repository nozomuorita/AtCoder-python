from collections import deque
N, D = map(int, input().split())
p = []
for i in range(N):
    xy = list(map(int, input().split()))
    p.append(xy)
    
# 感染したかどうか
inf = []
inf.append(True)
for i in range(1, N):
    inf.append(False)
    
# 事前に距離計算
tikai = [[] for i in range(N)]
for i in range(N):
    for j in range(i, N):
        if i==j:
            continue
        else:
            xy1 = p[i]
            xy2 = p[j]
            dist = (((xy1[0] - xy2[0])**2) + ((xy1[1] - xy2[1])**2)) ** 0.5
            if dist <= D:
                tikai[i].append(j)
                tikai[j].append(i)
                
new = 100
a = deque()
a.append(0)
while (len(a) != 0):
    n = a.popleft()
    tmp = tikai[n]
    for i in tmp:
        if inf[i] == False:
            inf[i] = True
            a.append(i)

for i in range(N):
    if inf[i]:
        print('Yes')
    else:
        print('No')