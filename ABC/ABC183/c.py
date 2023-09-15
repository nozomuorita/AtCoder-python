import sys
sys.setrecursionlimit(100000000)

n, k = map(int, input().split())
t = []

for i in range(n):
    t_ = list(map(int, input().split()))
    t.append(t_)
    
ans = 0
visited = [False] * n
visited[0] = True

def dfs(i, cost):
    global ans
    if visited.count(True) == n:
        cost += t[i][0]
        if cost == k:
            ans += 1
        
    for j in range(1, n):
        if visited[j]:
            continue
        visited[j] = True
        dfs(j, cost+t[i][j])
        visited[j] = False
        
dfs(0, 0)
print(ans)

# 別解(itertools)
# from itertools import permutations

# n, k = map(int, input().split())
# t = []
# for i in range(n):
#     _ = list(map(int, input().split()))
#     t.append(_)
    
# ans = 0
# l = list(range(1, n))
# s = permutations(l, n-1)

# for i in s:
#     pre, cost = 0, 0
#     for j in i:
#         cost += t[pre][j]
#         pre = j
#     cost += t[pre][0]
#     if cost == k:
#         ans += 1
        
# print(ans)