import sys
from collections import defaultdict
sys.setrecursionlimit(100000000)

n = int(input())
visited = [False] * n
ans = -1

# g = []
# for i in range(n-1):
#     tmp = list(map(int, input().split()))
#     g.append(tmp)
g = defaultdict(int)
for i in range(n-1):
    tmp = list(map(int, input().split()))
    tmp_n = i+1
    for j in tmp:
        g[(i, tmp_n)] = j
        tmp_n += 1
print(g)
    
def dfs(i, cost):
    global ans
    global visited
    visited[i] = True
    if visited.count(True)==n:
        if cost>ans:
            ans = cost
            print(f'aaa: {cost}{i}')
    
    for j in range(n):
        if (visited[j]) or (i==j):
            continue
        print(i, j)
        #cost += g[min(i, j)][max(i, j)]
        cost += g[(min(i, j), max(i, j))]
        visited[j] = True
        if visited.count(True)==n:
            if cost>ans:
                ans = cost
                print(f'aaa: {cost}, {i}')
        else:
            for k in range(n):
                if (visited[k]):
                    continue
                else:
                    dfs(k, cost)
                    visited[j] = False
    visited[i] = False
        
    #visited[k] = False

dfs(0, 0)
print(ans)