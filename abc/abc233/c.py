import sys
sys.setrecursionlimit(100000000)

n, x = map(int, input().split())
l, a = [], []
ans = 0

for i in range(n):
    tmp = list(map(int, input().split()))
    l.append(tmp[0])
    a.append(tmp[1:])
    
def dfs(i, j):
    global ans
    global n
    if i > x:
        return
    if (j == n-1) and (i == x):
        ans += 1
        return
    
    if j < (n-1):
        for k in a[j+1]:
            dfs(i*k, j+1)
            
for m in range(len(a[0])):
    dfs(a[0][m], 0)
    
print(ans)