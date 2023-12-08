import sys
sys.setrecursionlimit(100000000)

n = int(input())
a = []
for i in range(2*n-1):
    tmp = ([0]*(i+1)) + list(map(int, input().split()))
    a.append(tmp)

ans = -1
used = [False]*(2*n)
# cnt: 見た人数, score: 楽しさ
def dfs(cnt, score):
    global ans
    if cnt==(2*n):
        ans = max(ans, score)
        return
    
    i = used.index(False)
    used[i] = True
    for j in range(i+1, 2*n):
        if used[j]: continue
        used[j] = True
        dfs(cnt+2, score^a[min(i, j)][max(i, j)])
        used[j] = False
        
    used[i] = False
    
dfs(0, 0)
print(ans)