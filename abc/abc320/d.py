"""
・dfsかbfsで近い頂点から探索して、座標を確定していく
"""

# bfs
from collections import deque, defaultdict

n, m = map(int, input().split())
ans = defaultdict(list)
g = defaultdict(list)
for i in range(m):
    a, b, x, y = map(int, input().split())
    g[a-1].append([b-1, x, y])
    g[b-1].append([a-1, -x, -y])

q = deque()
q.append([0, 0, 0])

while q:
    i, x, y = q.popleft()
    if len(ans[i])!=0: continue
    
    ans[i] = [x, y]
    for j, x2, y2 in g[i]:
        q.append([j, x+x2, y+y2])
        
for i in range(n):
    if len(ans[i])==0:
        print('undecidable')
    else:
        print(*ans[i])
        

# # dfs
# from collections import defaultdict
# import sys
# sys.setrecursionlimit(100000000)

# n, m = map(int, input().split())
# ans = defaultdict(list)
# g = defaultdict(list)
# for i in range(m):
#     a, b, x, y = map(int, input().split())
#     g[a-1].append([b-1, x, y])
#     g[b-1].append([a-1, -x, -y])
    
# visited = [False] * n

# def dfs(i, x_pos, y_pos):
#     visited[i] = True
#     ans[i] = [x_pos, y_pos]
    
#     for j, x, y in g[i]:
#         if visited[j]:
#             continue
#         dfs(j, x_pos+x, y_pos+y)
        
# dfs(0, 0, 0)

# for i in range(n):
#     if len(ans[i])==0:
#         print('undecidable')
#     else:
#         print(*ans[i])