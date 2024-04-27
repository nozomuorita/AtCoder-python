import sys
sys.setrecursionlimit(100000000)
h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
D = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(i, j):
    global cnt, st
    cnt += 1
    visited[i][j] = True
    
    f = True
    for d1, d2 in D:
        if 0<=i+d1<h and 0<=j+d2<w:
            if s[i+d1][j+d2]=="#":
                f = False
                st.add((i, j))
                break
    if f:
        for d1, d2 in D:
            if 0<=i+d1<h and 0<=j+d2<w:
                if s[i+d1][j+d2]!="#" and visited[i+d1][j+d2]==False:
                    dfs(i+d1, j+d2)
    
visited = [[False]*w for _ in range(h)]
ans = 1
for i in range(h):
    for j in range(w):
        if visited[i][j]: continue
        if s[i][j]=="#": continue
        cnt = 0
        st = set()
        dfs(i, j)
        ans = max(ans, cnt)
        for i2, j2 in st:
            visited[i2][j2] = False

print(ans)