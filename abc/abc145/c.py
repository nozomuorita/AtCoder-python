import sys
sys.setrecursionlimit(100000000)
n = int(input())
xy = [list(map(int, input().split())) for i in range(n)]

#  各町間の距離を事前計算
dist = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(i+1, n):
        d = ((xy[i][0]-xy[j][0])**2 + (xy[i][1]-xy[j][1])**2)**0.5
        dist[i][j] = d
        dist[j][i] = d

s = 0
l = 0

def dfs(town, score):
    global s, l
    if len(town)==n:
        s += score
        l += 1
        return
    
    for i in range(n):
        if i in town: continue
        if len(town)==0: dfs([i], 0)
        else:
            score2 = score + dist[town[-1]][i]
            dfs(town+[i], score2)
        
dfs([], 0)

ans = s/l
print(ans)