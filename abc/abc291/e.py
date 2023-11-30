from collections import deque
n, m = map(int, input().split())
g = [[] for _ in range(n)]
nyujisu = [0]*n               #  入次数
for i in range(m):
    x, y = map(lambda x: x-1, map(int, input().split()))
    g[y].append(x)
    nyujisu[x] += 1
    
q = deque()
#  探索可能頂点数
v_num = 0
for i in range(n):
    if nyujisu[i]==0: v_num+=1; q.append(i)
    
if v_num!=1: exit(print('No'))

order = [0]*n
rem = n
while True:
    now = q.popleft()
    v_num -= 1
    order[now] = rem
    rem -= 1
    
    #  全位置を決定できたら終了
    if rem==0: break
    
    for nxt in g[now]:
        nyujisu[nxt] -= 1
        if nyujisu[nxt]==0:
            q.append(nxt)
            v_num += 1
    
    if v_num!=1: exit(print('No'))
    
print('Yes')
print(*order)


# from collections import defaultdict, deque
# N, M = map(int, input().split())
# gout = defaultdict(list)
# deg = [0]*N
# for _ in [0]*M:
#     x, y = map(int, input().split())
#     gout[x-1].append(y-1)
#     deg[y-1] += 1

# ans = [0]*N
# que = deque([])
# cnt = 0
# for i in range(N):
#     if deg[i] == 0: que.append(i)

# while len(que) > 0:
#     if len(que) != 1:
#         print("No")
#         exit()
#     v = que.popleft()
#     cnt += 1
#     ans[v] = cnt

#     for next in gout[v]:
#         deg[next] -= 1
#         if deg[next] == 0:
#             que.append(next)

# print("Yes")
# for i in range(N):
#     print(ans[i], end=" ")