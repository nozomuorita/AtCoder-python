from collections import deque
n = int(input())
g = [[] for _ in range(n)]
into = [0]*n
for i in range(n):
    c, *p = map(int, input().split())
    for j in p:
        g[i].append(j-1)
        into[j-1] += 1

# bfs
q = deque([0])
dist = [-1]*n
dist[0] = 0
node = []
while q:
    v = q.popleft()
    node.append(v)
    for v2 in g[v]:
        if dist[v2]!=-1: continue
        dist[v2] = dist[v] + 1
        q.append(v2)

# トポソ
def topological_sort(G, into_num):
    #入ってくる有向辺を持たないノードを列挙
    q = deque()
    #V: 頂点数
    for i in range(n):
        if into_num[i]==0:
            q.append(i)
    
    #以下、幅優先探索
    ans = []
    while q:
        v = q.popleft()
        ans.append(v)
        for adj in G[v]:
            into_num[adj] -= 1 #入次数を減らす
            if into_num[adj]==0:
                q.append(adj) #入次数が0になったら、キューに入れる
    
    return ans

ans = topological_sort(g, into)
for i in reversed(ans):
    if dist[i]==-1: continue
    if i==0: break
    print(i+1, end=" ")
