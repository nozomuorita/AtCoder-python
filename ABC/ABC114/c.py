import sys
sys.setrecursionlimit(100000000)

n = int(input())
ans = 0

def dfs(i, use3, use5, use7):
    global ans
    if i > n:
        return
    if use3 and use5 and use7:
        ans += 1
    dfs(10*i+3, True, use5, use7)
    dfs(10*i+5, use3, True, use7)
    dfs(10*i+7, use3, use5, True)
            
dfs(0, False, False, False)
print(ans)
