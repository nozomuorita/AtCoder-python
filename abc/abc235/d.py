from collections import deque
a, n = map(int, input().split())
l = 10**(len(str(n)))
    
q = deque()
q.append(1)
dist = [-1] * l
dist[1] = 0

while q:
    v = q.popleft()
    
    if (v*a)<l and dist[v*a]==-1:
        dist[v*a] = dist[v] + 1
        q.append(v*a)
    
    if v>=10 and v%10!=0:
        t = int(str(v)[-1] + str(v)[:-1])
        if t<l and dist[t]==-1:
            dist[t] = dist[v] + 1
            q.append(t)
            
print(dist[n])