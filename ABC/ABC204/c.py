from collections import deque
n, m = map(int, input().split())
g = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)

# 各頂点を始点として、到達できる点を数えていく
# 頂点iについて、(i, i)は確実に到達できるので事前にansに足しておく(以下の処理中では、足さないようにする)
ans = n
# 到達できる組み合わせ(始点、終点)を管理
pair = set()
for i in range(n):
    # 頂点iを始点として、BFS
    q = deque([i])
    visited = [False] * n
    visited[i] = True
    while q:
        j = q.popleft()
        visited[j] = True
        if i != j:
            # iとjが異なり、まだ見つけていない組み合わせならばansを１足す
            if (i, j) not in pair:
                ans += 1
                pair.add((i, j))
        for k in g[j]:
            if visited[k]:
                continue
            q.append(k)
            
print(ans)