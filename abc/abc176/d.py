from collections import deque
h, w = map(int, input().split())
sh, sw = map(lambda x:x-1, map(int, input().split()))
gh, gw = map(lambda x:x-1, map(int, input().split()))
s = [input() for _ in range(h)]

q = deque()
q.append((sh, sw, 0))
dist = [[1<<60]*w for _ in range(h)]
dist[sh][sw] = 0

while q:
    x, y, d = q.popleft()
    if dist[x][y]!=d: continue
    
    for d1, d2 in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        th, tw = x+d1, y+d2
        
        if not(0<=th<h) or not(0<=tw<w) or s[th][tw]=="#" or dist[th][tw]<=dist[x][y]:
            continue
        dist[th][tw] = d
        q.appendleft((th, tw, d))
    
    for d1 in range(-2, 3):
        for d2 in range(-2, 3):
            if d1==0 and d2==0: continue
            th, tw = x+d1, y+d2
            if not(0<=th<h) or not(0<=tw<w) or s[th][tw]=="#" or dist[th][tw]<=dist[x][y]+1:
                continue
            dist[th][tw] = d+1
            q.append((th, tw, d+1))

print(-1) if dist[gh][gw]==1<<60 else print(dist[gh][gw])