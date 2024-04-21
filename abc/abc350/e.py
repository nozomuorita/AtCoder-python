import sys
sys.setrecursionlimit(100000000)
n, a, x, y = map(int, input().split())
memo = {}
memo[0] = 0

def dfs(n):
    global x, y
    if n==0: return 0
    if n in memo:
        return memo[n]

    p1 = x + dfs(n//a)
    p2 = (6/5)*y
    for i in range(2, 6+1):
        p2 += (1/5)*dfs(n//i)
    
    memo[n] = min(p1, p2)
    return memo[n]

ans = dfs(n)
print(ans)